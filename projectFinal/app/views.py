from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import TranslationForm, SignUpForm
from .models import Translation
from django.contrib import messages
from transformers import pipeline

# the django documentation was used to learn how to comeplete forms and other features such
# as log in. https://docs.djangoproject.com/en/5.0/topics/auth/default/

def home(request):

    translated_text = ''

    # default values start with English to Spanish
    language_from = 'English'  
    language_to = 'Spanish'    

    if request.method == 'POST':
        post_data = request.POST.copy()

        #get the language to and from
        language_from = post_data.get('language_from', 'English')  
        language_to = post_data.get('language_to', 'Spanish')      
        language_direction = f"{language_from}_to_{language_to}"

        post_data['language_direction'] = language_direction
        form = TranslationForm(post_data)

        if form.is_valid():
            text_to_translate = form.cleaned_data['text_to_translate']
            language_direction = form.cleaned_data['language_direction']

            # use the pipeline for translation depending on the direction of translation
            translator = None
            if language_direction == 'en_to_es':
                translator = pipeline("translation_en_to_es", model="beanslmao/helsinki-en-es-fine-tune-opus100")
            elif language_direction == 'es_to_en':
                translator = pipeline("translation_es_to_en", model="beanslmao/helsinki-es-en-opus100-fine-tuned")

            # translates the text
            if translator:
                print("Translator working")
                translationResults = translator(text_to_translate)
                translated_text = translationResults[0]['translation_text']
                
            # if logged in, saves the translation for later access in their profile.
                if request.user.is_authenticated:
                    Translation.objects.create(
                        user=request.user,
                        original_text = text_to_translate,
                        translated_text = translated_text,
                        language_direction = language_direction
                    )
        else:
            print("Form submission failed, below is the error:")
            print(form.errors)
    else:
        form = TranslationForm()

    return render(request, 'app/home.html', {
        'form': form,
        'translated_text': translated_text,
        'language_from': language_from,  
        'language_to': language_to,      
    })


# the profile and log out features are obviously only available when already logged in.
@login_required
def profile(request):
    user_translations = request.user.translation_set.all()
    return render(request, 'app/profile.html', {'translations': user_translations})

@login_required
def user_logout(request):
    logout(request)
    messages.warning(request, 'You have logged out successfully.')
    return redirect('home')

# sign up, credentials are provided, if valid then a user is made and then logged in. 
# signup method inspired from https://stackoverflow.com/questions/48049498/django-usercreationform-custom-fields
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            passwordInput = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=passwordInput)

            login(request, user)

            messages.success(request, 'Sign up is successful. You are now logged in')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})

# user login, checks if the credentials are correct and if so redirect to the home page for translation.
# inspired by https://docs.djangoproject.com/en/5.0/topics/auth/default/
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'You have logged in successfully.')
                return redirect('home')    
        else:
            messages.error(request, 'The login credentials provided were incorrect.')
            return redirect('login')

    else:
        return render(request, 'app/login.html')
