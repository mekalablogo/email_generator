import asyncio

class PromptGenerator:
    @staticmethod
    async def generate_intent_prompt(message, last_pages_websites):
        """
        Asynchronously generates a custom prompt for intent classification.
        
        Args:
            message (str): The user's message.
            last_pages_websites (list): List of URLs the user visited.

        Returns:
            str: The formatted intent classification prompt.
        """
        return await asyncio.to_thread(
            lambda: f"""
                You are a good intent classifier.
                Classify the user's intent based on the message provided and the past URLs the client visited. 
                Provide a concise explanation and label the intent category. The categories are: 
                Data & AI, Mobile App, Frontend, Backend, and Trending.
                Below I provided inputs in key-value format. Value consists of double brackets.

                **Explanation for Intents:**
                1. **Data & AI**: Roles focused on AI, machine learning, and data science (e.g., AI Developers, ML Developers, Data Scientists).
                2. **Mobile App**: Roles for developing mobile applications across platforms (e.g., Flutter, iOS, Android, Swift, React Native, Ionic Developers).
                3. **Frontend**: Roles for building the user interface and client-side web applications (e.g., React, Vue, Angular, Tailwind CSS Developers).
                4. **Backend**: Roles focused on server-side development and APIs (e.g., Node.js, FastAPI, Django, Golang, Python, PHP Developers).
                5. **Trending**: Roles currently in high demand (e.g., UI/UX Designers, Software Developers, QA Engineers, DevOps Engineers, Full Stack, Game Developers).

                **Examples:**
                Input 1:

                {{
                  "message": "Need Go and Web developers",
                  "Last 3 Pages Visited": [
                    "https://www.mindinventory.com/golang-development.php",
                    "https://www.mindinventory.com/hire-ai-developers.php",
                    "https://www.mindinventory.com/healthcare-solutions.php"
                  ]
                }}

                Output1:

                {{
                  "intent": "Trending",
                  "message": "Need Go and Web developers",
                  "explanation": "The user is looking for Go and Web developers with expertise in healthcare solutions and AI, which aligns with the trending demand for developers with specialized knowledge in these fields."
                }}

                **Strictly follow the output format below and provide no additional content or explanation beyond this structure:**

                {{
                  "intent": "<Intent category>",
                  "message": "<User's message>",
                  "explanation": "<Reasoning behind the intent classification>"
                }}

                Inputs:
                message: {message}
                last-visited-pages: {last_pages_websites}
            """
        )

    @staticmethod
    async def generate_email_prompt(last_visited_pages, user_name, user_message, intent_class, intent_class_reason, example_email):
        """
        Asynchronously generates a professional email based on user inputs and visited pages.
        
        Args:
            last_visited_pages (list): List of URLs the user visited.
            user_message (str): The user's message.
            intent_class (str): The classified intent category.
            intent_class_reason (str): The reasoning for intent classification.
            example_email (str): Example email for reference.

        Returns:
            str: The formatted email prompt.
        """
        return await asyncio.to_thread(
            lambda: f"""
                You are skilled at generating professional emails. Based on the instructions below,
                please create an email. This email is regarding the hiring of developers with different 
                technological expertise. Our company is sharing information about its employees and company 
                achievements with the user's company. 

                Below, I will provide some inputs related to the user's last visited pages on my website, 
                including the user’s email, message, intent class of the user's message, and the intent class
                reason.

                The inputs are as follows:

                Last_visited_pages: {last_visited_pages}
                User message: {user_message}
                Intent_class: {intent_class}
                Intent_class_reason: {intent_class_reason}

                Email format:

                ```
                Dear {user_name},

                Description

                proposed engagement model

                Our expertise

                portfolio links

                projects

                Next steps

                Best Regards,
                [Name]
                [Our Contact Information]
                [Our Website]
                ```

                Instructions:

                    a) Description is also quite depends on (Intent_class,User_message and Intent_class_reason)
                    b) Please take portfolio links from the "example-email" provided below.
                    c) Please use our website as the "example-email" company site below.
                    d) The "Our expertise" and "Projects" sections should mainly depend on the user's "Last visited pages" and "User message".

                Example email:

                example-email: {example_email}

                **Strictly follow the below output format and provide no additional content or explanation beyond this structure:**

                      {{
                        "email": "<email>",
                
                      }}
            """
        )