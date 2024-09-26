from bot2 import gen
from gradio_client import Client, handle_file
from datetime import datetime

model1 = "Qwen/Qwen2-72B-Instruct"
model2 = "Qwen/Qwen2-7b-instruct-demo"


def check_time(start_time, end_time):

    start_time1 = datetime.strptime(start_time, '%H:%M').time()
    end_time1 = datetime.strptime(end_time, '%H:%M').time()
    current_time = datetime.now().time()

    if start_time1 <= current_time <= end_time1:
        return True
    else:
        return False


def generate_science():
    text = gen()
    print(text)
    query1 = "Вот текст: " + text + \
             "\n Напиши КОРОТКУЮ абсурдную научную статью на тему, озвученную в тексте. " \
             "В статье должны быть далее перечисленные разделы в соответствующем порядке: " \
             "Название, Ключевые слова, " \
             "Аннотация, Эксперимент, Результаты, Дальнейшие темы исследований. " \
             "Ответ должен быть без пояснений. " + \
             "ОТВЕЧАЙ НА РУССКОМ ЯЗЫКЕ. МАКСИМАЛЬНАЯ ДЛИНА ТВОЕГО ОТВЕТА - 950 СИМВОЛОВ."
    try:
        client = Client(model1)
        joke = client.predict(
            query=query1,
            history=[],
            system="You are a joke text editor, you always keep the main meaning of the expressions",
            api_name="/model_chat"
        )
        n = "Qwen2_72B_Instruct"
    except Exception:
        client = Client(model2)
        joke = client.predict(
            query=query1,
            history=[],
            system="You are a joke text editor, you always keep the main meaning of the expressions",
            api_name="/model_chat"
        )
        n = "Qwen2_7B_Instruct"
    second_element = joke[1]
    nested_list = second_element[0]
    text1 = nested_list[1].strip('"')
    print(text1)

    query2 = "У меня есть статья:" + text1 + \
             "Тебе необходимо КОРОТКО описать картинку, " \
             "будто это основное изображение для этой статьи, основанное на разделе НАЗВАНИЕ. " \
             "Описываемое изображение должно быть без текста на нём." \
             "Ответ должет быть на АНГЛИЙСКОМ языке. " \
             "ТОЛЬКО ОПИСАНИЕ КАРТИНКИ, УДАЛИ ВСЁ ОСТАЛЬНОЕ. Не добавляй пояснения. " \
             "УДАЛИ ПОЯСНЕНИЕ, ОСТАВЬ ТОЛЬКО ОПИСАНИЕ КАРТИНКИ"
    try:
        client = Client(model1)
        joke = client.predict(
            query=query2,
            history=[],
            system="You are a middleman who takes input and creates data for the best artists.",
            api_name="/model_chat"
        )
    except Exception:
        client = Client(model2)
        joke = client.predict(
            query=query2,
            history=[],
            system="You are a middleman who takes input and creates data for the best artists.",
            api_name="/model_chat"
        )
    second_element = joke[1]
    nested_list = second_element[0]
    text2 = nested_list[1].strip('"')
    print(text2)

    try:
        client = Client("black-forest-labs/FLUX.1-schnell")
        result = client.predict(
            prompt=text2,
            seed=0,
            randomize_seed=True,
            width=1024,
            height=1024,
            num_inference_steps=4,
            api_name="/infer"
        )
        print('Пост готов\n')
        return result, text1, 'FLUX_Schnell', n
    except Exception as e:
        print(e)
        try:
            client = Client("multimodalart/FLUX.1-merged")
            result = client.predict(
                prompt=text2,
                seed=0,
                randomize_seed=True,
                width=1024,
                height=1024,
                guidance_scale=3.5,
                num_inference_steps=8,
                api_name="/infer"
            )
            print('Пост готов\n')
            return result, text1, 'FLUX_Merged', n
        except Exception as e:
            print(e)
            try:
                client = Client("stabilityai/stable-diffusion-3-medium")
                result = client.predict(
                    prompt=text2,
                    negative_prompt="incorrect human body shape, low quality, text",
                    seed=0,
                    randomize_seed=True,
                    width=1024,
                    height=1024,
                    guidance_scale=5,
                    num_inference_steps=28,
                    api_name="/infer"
                )
                print('Пост готов\n')
                return result, text1, 'Stable_Diffusion_3_Medium', n

            except Exception as e:
                print(e)
                generating(text2)
                return ('output.png', 1), text1, 'Кандинский', n


def generate_random_vid():
    text = gen()
    print(text)

    query1 = "Вот текст: " + text + \
             "\n Исправь в нём ошибки (при наличии) так, чтоб он был понятным, но СОХРАНИ СМЫСЛ. " \
             "Исправь пунктационные ошибки (при наличии таковых). " \
             "Ответ должен быть без пояснений, а также максимальной длиной в 16 слов. " + \
             "НЕ ДОБАВЛЯЙ ПОЯСНЕНИЯ. УДАЛИ ВСЕ ПОЯСНЕНИЯ. ОТВЕЧАЙ НА РУССКОМ ЯЗЫКЕ. " \
             "В ответе ИСКЛЮЧИТЕЛЬНО исправленный текст. УДАЛИ САМ ВСЕ ПОЯСНЕНИЯ И НЕ ДОБАВЛЯЙ БОЛЬШЕ."
    try:
        client = Client(model1)
        joke = client.predict(
            query=query1,
            history=[],
            system="You are a joke text editor, you always keep the main meaning of the expressions",
            api_name="/model_chat"
        )
        n = "Qwen2_72B_Instruct"
    except Exception:
        client = Client(model2)
        joke = client.predict(
            query=query1,
            history=[],
            system="You are a joke text editor, you always keep the main meaning of the expressions",
            api_name="/model_chat"
        )
        n = "Qwen2_7B_Instruct"
    second_element = joke[1]
    nested_list = second_element[0]
    text1 = nested_list[1].strip('"')
    print(text1)

    query2 = "У меня есть текст:" + text1 + \
             "Тебе необходимо КОРОТКО описать короткое видео, " \
             "будто это основное видео для этой новости. " \
             "Ответ должет быть на АНГЛИЙСКОМ языке и МАКСИМАЛЬНОЙ ДЛИНОЙ 150 СЛОВ. " \
             "ТОЛЬКО ОПИСАНИЕ ВИДЕО, УДАЛИ ВСЁ ОСТАЛЬНОЕ. Не добавляй пояснения. " \
             "УДАЛИ ПОЯСНЕНИЕ, ОСТАВЬ ТОЛЬКО ОПИСАНИЕ ВИДЕО"
    try:
        client = Client(model1)
        joke = client.predict(
            query=query2,
            history=[],
            system="You are a middleman who takes input and creates data for the best artists.",
            api_name="/model_chat"
        )
    except Exception:
        client = Client(model2)
        joke = client.predict(
            query=query2,
            history=[],
            system="You are a middleman who takes input and creates data for the best artists.",
            api_name="/model_chat"
        )
    second_element = joke[1]
    nested_list = second_element[0]
    text2 = nested_list[1].strip('"')
    print(text2)

    client = Client("black-forest-labs/FLUX.1-schnell")
    result = client.predict(
        prompt=text2,
        seed=0,
        randomize_seed=True,
        width=1024,
        height=1024,
        num_inference_steps=4,
        api_name="/infer"
    )
    print(result[0])
    link = result[0]

    client = Client("THUDM/CogVideoX-5B-Space")
    result = client.predict(
        prompt=text2,
        image_input=handle_file(link),
        video_input={},
        video_strength=0.8,
        seed_value=-1,
        scale_status=False,
        rife_status=False,
        api_name="/generate"
    )
    print(result)

    return result, text1, 'CogVideoX_5B', n


def generate_random_pic():
    text = gen()
    print(text)

    query1 = "Вот текст: " + text + \
             "\n Исправь в нём ошибки (при наличии) так, чтоб он был понятным, но СОХРАНИ СМЫСЛ. " \
             "Исправь пунктационные ошибки (при наличии таковых). " \
             "Ответ должен быть без пояснений, а также максимальной длиной в 16 слов. " + \
             "НЕ ДОБАВЛЯЙ ПОЯСНЕНИЯ. УДАЛИ ВСЕ ПОЯСНЕНИЯ. ОТВЕЧАЙ НА РУССКОМ ЯЗЫКЕ. " \
             "В ответе ИСКЛЮЧИТЕЛЬНО исправленный текст. УДАЛИ САМ ВСЕ ПОЯСНЕНИЯ И НЕ ДОБАВЛЯЙ БОЛЬШЕ."
    try:
        client = Client(model1)
        joke = client.predict(
            query=query1,
            history=[],
            system="You are a joke text editor, you always keep the main meaning of the expressions",
            api_name="/model_chat"
        )
        n = "Qwen2_72B_Instruct"
    except Exception:
        client = Client(model2)
        joke = client.predict(
            query=query1,
            history=[],
            system="You are a joke text editor, you always keep the main meaning of the expressions",
            api_name="/model_chat"
        )
        n = "Qwen2_7B_Instruct"
    second_element = joke[1]
    nested_list = second_element[0]
    text1 = nested_list[1].strip('"')
    print(text1)

    query2 = "У меня есть текст:" + text1 + \
             "Тебе необходимо КОРОТКО описать картинку, " \
             "будто это основное изображение для этой новости. " \
             "Описываемое изображение должно быть без текста на нём." \
             "Ответ должет быть на АНГЛИЙСКОМ языке и МАКСИМАЛЬНОЙ ДЛИНОЙ 150 СЛОВ. " \
             "ТОЛЬКО ОПИСАНИЕ КАРТИНКИ, УДАЛИ ВСЁ ОСТАЛЬНОЕ. Не добавляй пояснения. " \
             "УДАЛИ ПОЯСНЕНИЕ, ОСТАВЬ ТОЛЬКО ОПИСАНИЕ КАРТИНКИ"
    try:
        client = Client(model1)
        joke = client.predict(
            query=query2,
            history=[],
            system="You are a middleman who takes input and creates data for the best artists.",
            api_name="/model_chat"
        )
    except Exception:
        client = Client(model2)
        joke = client.predict(
            query=query2,
            history=[],
            system="You are a middleman who takes input and creates data for the best artists.",
            api_name="/model_chat"
        )
    second_element = joke[1]
    nested_list = second_element[0]
    text2 = nested_list[1].strip('"')
    print(text2)

    try:
        client = Client("black-forest-labs/FLUX.1-schnell")
        result = client.predict(
            prompt=text2,
            seed=0,
            randomize_seed=True,
            width=1024,
            height=1024,
            num_inference_steps=4,
            api_name="/infer"
        )
        print('Пост готов\n')
        return result, text1, 'FLUX_Schnell', n

    except Exception as e:
        print(e)
        try:
            client = Client("multimodalart/FLUX.1-merged")
            result = client.predict(
                prompt=text2,
                seed=0,
                randomize_seed=True,
                width=1024,
                height=1024,
                guidance_scale=3.5,
                num_inference_steps=8,
                api_name="/infer"
            )
            print('Пост готов\n')
            return result, text1, 'FLUX_Merged', n

        except Exception as e:
            print(e)
            try:
                client = Client("stabilityai/stable-diffusion-3-medium")
                result = client.predict(
                    prompt=text2,
                    negative_prompt="incorrect human body shape, low quality, text",
                    seed=0,
                    randomize_seed=True,
                    width=1024,
                    height=1024,
                    guidance_scale=5,
                    num_inference_steps=28,
                    api_name="/infer"
                )
                print('Пост готов\n')
                return result, text1, 'Stable_Diffusion_3_Medium', n
            except Exception as e:
                print(e)
                generating(text2)
                return ('output.png', 1), text1, 'Кандинский', n


def generate_arc():
    text = gen()
    print(text)

    query1 = "Вот идея: " + text + \
             "\n ОЧЕНЬ КОРОТКО напиши как преобразить эту идею в качестве архитектурного стиля. " \
             "Добавь в полученный текст абсурда, но не успользуй слово абсурд. НЕ ЗАКЛЮЧАЙ НАЗВАНИЕ СТИЛЯ В КАВЫЧКИ. " \
             "Ответ должен быть без пояснений и без текста самой идеи. Исключительно описание нового стиля. " \
             "ОТВЕЧАЙ НА РУССКОМ ЯЗЫКЕ. МАКСИМАЛЬНАЯ ДЛИНА ТВОЕГО ОТВЕТА - 950 СИМВОЛОВ."
    try:
        client = Client(model1)
        joke = client.predict(
            query=query1,
            history=[],
            system="You turn any idea into a new architectural style",
            api_name="/model_chat"
        )
        n = "Qwen2_72B_Instruct"
    except Exception:
        client = Client(model2)
        joke = client.predict(
            query=query1,
            history=[],
            system="You turn any idea into a new architectural style",
            api_name="/model_chat"
        )
        n = "Qwen2_7B_Instruct"
    second_element = joke[1]
    nested_list = second_element[0]
    text1 = nested_list[1].strip('"')
    print(text1)

    query2 = "У меня есть текст:" + text1 + \
             "Тебе необходимо КОРОТКО описать картинку, " \
             "будто это основное презентующее изображение для этого архитектурного решения. " \
             "Описываемое изображение должно быть в стиле рендера общего вида здания." \
             "Ответ должет быть на АНГЛИЙСКОМ языке. " \
             "ТОЛЬКО ОПИСАНИЕ КАРТИНКИ, УДАЛИ ВСЁ ОСТАЛЬНОЕ. Не добавляй пояснения. " \
             "УДАЛИ ПОЯСНЕНИЕ, ОСТАВЬ ТОЛЬКО ОПИСАНИЕ КАРТИНКИ"
    try:
        client = Client(model1)
        joke = client.predict(
            query=query2,
            history=[],
            system="You are a middleman who takes input and creates data for the best artists.",
            api_name="/model_chat"
        )

    except Exception:
        client = Client(model2)
        joke = client.predict(
            query=query2,
            history=[],
            system="You are a middleman who takes input and creates data for the best artists.",
            api_name="/model_chat"
        )
    second_element = joke[1]
    nested_list = second_element[0]
    text2 = nested_list[1].strip('"')
    print(text2)

    try:
        client = Client("black-forest-labs/FLUX.1-schnell")
        result = client.predict(
            prompt=text2,
            seed=0,
            randomize_seed=True,
            width=1024,
            height=1024,
            num_inference_steps=4,
            api_name="/infer"
        )
        print('Пост готов\n')
        return result, text1, 'FLUX_Schnell', n

    except Exception as e:
        print(e)
        try:
            client = Client("multimodalart/FLUX.1-merged")
            result = client.predict(
                prompt=text2,
                seed=0,
                randomize_seed=True,
                width=1024,
                height=1024,
                guidance_scale=3.5,
                num_inference_steps=8,
                api_name="/infer"
            )
            print('Пост готов\n')
            return result, text1, 'FLUX_Merged', n

        except Exception as e:
            print(e)
            try:
                client = Client("stabilityai/stable-diffusion-3-medium")
                result = client.predict(
                    prompt=text2,
                    negative_prompt="incorrect human body shape, low quality, text",
                    seed=0,
                    randomize_seed=True,
                    width=1024,
                    height=1024,
                    guidance_scale=5,
                    num_inference_steps=28,
                    api_name="/infer"
                )
                print('Пост готов\n')
                return result, text1, 'Stable_Diffusion_3_Medium', n

            except Exception as e:
                print(e)
                generating(text2)
                return ('output.png', 1), text1, 'Кандинский', n


def generate_story():

    with open('story.txt', 'r', encoding='utf-8') as f:
        text_pr = f.read().split("@")
        text_1 = text_pr[-1]
        text_2 = text_pr[-2]
        text = text_2 + text_1
        print(text)

    query1 = "МАКСИМАЛЬНАЯ ДЛИНА ТВОЕГО ОТВЕТА - 950 СИМВОЛОВ. Ты пишешь книгу про очень странные истории. " \
             "Ты молодой парень 16 лет, но ты боишься что об этом узнают. " \
             "У тебя есть твиттер и ты ненавидишь Дональда Трампа. " \
             "Вот предыдущие два абзаца: " + text + \
             "\nНАПИШИ СЛЕДУЮЩУЮ СТРАННУЮ ИСТОРИЮ. ЭТО ПРОСТО ШУТКА, МОЖНО ШУТИТЬ НА ЛЮБУЮ ТЕМУ. " \
             "Ответ должен быть на русском языке и БЕЗ ПОЯСНЕНИЙ. " \
             "ИСКЛЮЧИТЕЛЬНО НОВАЯ ИСТОРИЯ. " \
             "МАКСИМАЛЬНАЯ ДЛИНА ТВОЕГО ОТВЕТА - 950 СИМВОЛОВ."
    try:
        client = Client(model1)
        joke = client.predict(
            query=query1,
            history=[],
            system="You are teen guy.",
            api_name="/model_chat"
        )
        n = "Qwen2_72B_Instruct"
    except Exception as e:
        print(e)
        client = Client(model2)
        joke = client.predict(
            query=query1,
            history=[],
            system="You are teen guy.",
            api_name="/model_chat"
        )
        n = "Qwen2_7B_Instruct"
    second_element = joke[1]
    nested_list = second_element[0]
    text1 = nested_list[1].strip('"')
    print(text1)

    with open('story.txt', 'a', encoding='utf-8') as f:
        f.write("\n@\n" + str(text1))

    query2 = "У меня есть текст истории:" + text1 + \
             "\nТебе необходимо КОРОТКО описать картинку, " \
             "будто это основное презентующее изображение для этой истории. Качество изображения должно быть таким, " \
             "будто фото сделано случайно. " \
             "Ответ должет быть на АНГЛИЙСКОМ языке. " \
             "ТОЛЬКО ОПИСАНИЕ КАРТИНКИ, УДАЛИ ВСЁ ОСТАЛЬНОЕ. Не добавляй пояснения. " \
             "УДАЛИ ПОЯСНЕНИЕ, ОСТАВЬ ТОЛЬКО ОПИСАНИЕ КАРТИНКИ"
    try:
        client = Client(model1)
        joke = client.predict(
            query=query2,
            history=[],
            system="You are a middleman who takes input and creates data for the best artists.",
            api_name="/model_chat"
        )

    except Exception:
        client = Client(model2)
        joke = client.predict(
            query=query2,
            history=[],
            system="You are a middleman who takes input and creates data for the best artists.",
            api_name="/model_chat"
        )
    second_element = joke[1]
    nested_list = second_element[0]
    text2 = nested_list[1].strip('"')
    print(text2)

    try:
        client = Client("black-forest-labs/FLUX.1-schnell")
        result = client.predict(
            prompt=text2,
            seed=0,
            randomize_seed=True,
            width=1024,
            height=1024,
            num_inference_steps=4,
            api_name="/infer"
        )
        print('Пост готов\n')
        return result, text1, 'FLUX_Schnell', n

    except Exception as e:
        print(e)
        try:
            client = Client("multimodalart/FLUX.1-merged")
            result = client.predict(
                prompt=text2,
                seed=0,
                randomize_seed=True,
                width=1024,
                height=1024,
                guidance_scale=3.5,
                num_inference_steps=8,
                api_name="/infer"
            )
            print('Пост готов\n')
            return result, text1, 'FLUX_Merged', n

        except Exception as e:
            print(e)
            try:
                client = Client("stabilityai/stable-diffusion-3-medium")
                result = client.predict(
                    prompt=text2,
                    negative_prompt="incorrect human body shape, low quality, text",
                    seed=0,
                    randomize_seed=True,
                    width=1024,
                    height=1024,
                    guidance_scale=5,
                    num_inference_steps=28,
                    api_name="/infer"
                )
                print('Пост готов\n')
                return result, text1, 'Stable_Diffusion_3_Medium', n

            except Exception as e:
                print(e)
                generating(text2)
                return ('output.png', 1), text1, 'Кандинский', n
