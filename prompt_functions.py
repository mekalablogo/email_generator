from prompts import PromptGenerator
import asyncio

class EmailPromptGenerator(PromptGenerator):
    def __init__(self, last_visited_pages, user_name, user_message, intent_class, intent_class_reason, example_email):
        self.last_visited_pages = last_visited_pages
        self.user_name = user_name
        self.user_message = user_message
        self.intent_class = intent_class
        self.intent_class_reason = intent_class_reason
        self.example_email = example_email
    
    async def generate_email_prompt_template(self):
        """
        Asynchronously generates the final email prompt using the email prompt template.
        """
        return await asyncio.to_thread(
            super().generate_email_prompt,
            self.last_visited_pages,
            self.user_name,
            self.user_message,
            self.intent_class,
            self.intent_class_reason,
            self.example_email
        )

    @staticmethod
    async def email_messages(email_prompt):
        """
        Asynchronously generates messages from the email prompt.
        """
        return [
            {"role": "system", "content": "You are professional email generator."},
            {"role": "user", "content": f"{email_prompt}"},
        ]


class IntentPromptGenerator(PromptGenerator):
    def __init__(self, last_visited_websites, user_message):
        self.last_visited_websites = last_visited_websites
        self.user_message = user_message
    
    async def generate_intent_prompt_template(self):
        """
        Asynchronously generates the intent prompt dynamically.
        
        Returns:
            str: The generated intent prompt.
        """
        return await asyncio.to_thread(
            super().generate_intent_prompt,
            self.user_message,
            self.last_visited_websites
        )

    @staticmethod
    async def intent_messages(intent_prompt):
        """
        Asynchronously generates messages from the intent prompt.
        """
        return [
            {"role": "system", "content": "You are professional intent classifier."},
            {"role": "user", "content": f"{intent_prompt}"},
        ]

# Example usage
example_email = """Dear kumarpal ,

                    Thanks for your time over the call today. As discussed, since your app is currently ready and deployed, our first action item will focus on addressing ongoing issues, fixing bugs, and code refactoring to enhance app stability and performance followed by maintenance.

                    Since you've already invested significant time and effort in building and launching the app, the best course of action now is to streamline and optimize the current version before moving forward with new feature development. Our team will understand the current challenges you face and the objectives you are looking to achieve and will start working on the requirements accordingly. Our senior and experienced developers will take care of code review and refactoring, QA, Testing, Documentation, and implementing new features across platforms. Additionally, we have a team of skilled AI/ML developers who will assist in implementing AI features by ensuring compliance with relevant data protection and healthcare regulations.

                    We propose starting with an hourly model arrangement in which you can opt for a 100-hour bucket for which the pricing will be USD 1 million dollars (upfront payment). Once the hours are opted, we will assign an iOS developer, an Android developer, a Backend developer, and a Technical Manager to your project. They will collectively engage with you in a kick-off call to initiate the project, focusing on bug fixes, maintenance, and feature updates.

                    You will have direct access to the team through tools such as Skype, Slack, Basecamp, JIRA, or Asana, depending on your preference. This is going to be a flexible bucket model in which you will have the flexibility of having 1 or more resources working on the same or multiple projects simultaneously. This hourly bucket will have a validity of 2 to 3 months. The working days and times of the resources will be Mon-Fri, 8 hours a day, 10 am to 7 pm Indian Standard Time. Upon completion of the initial 100 hours, you can choose to continue with the same arrangement or transition to a dedicated resource engagement if additional features need to be added to the app.

                    Below I'm sharing some more information about MindInventory and links to the portfolio.
                    We are a Creative Design Studio and the New Age Digital Transformation Partner specializing in delivering cutting-edge digital solutions that empower businesses to thrive in today's rapidly evolving technological landscape. Over the years, we have leveraged our position in the global market with an enviable list of clients and a phenomenal growth rate achieved through IT innovation, dedicated teams, and timely implementation of solutions. We specialize in providing unique & creative designs; Graphic design to 2D, 3D Animations, and Motion graphics along with that having expertise in Web apps, Mobile apps, Game development, and much more that you can find on our company's websites https://www.mindinventory.com/ & https://300mind.studio/

                    Here I'm sharing the links to our overall portfolio:
                    https://dribbble.com/mindinventory
                    https://www.behance.net/mindinventory
                    https://www.mindinventory.com/all-portfolios.php
                    Here are the links to some of our projects in the Healthcare & Wellness domain.
                    Airofit: Stay a breath ahead
                    https://airofit.in/
                    https://play.google.com/store/apps/details?id=com.airofit_app&hl=en_IN
                    https://apps.apple.com/us/app/airofit/id1469023267
                    Biped AI: AI mobility vest for the blind
                    https://biped.ai/
                    Shoorah: Mental Health & Calm
                    https://shoorah.io/
                    https://play.google.com/store/apps/details?id=com.shoorah
                    https://apps.apple.com/us/app/shoorah-mental-health-calm/id1669683359
                    Biostrap:
                    https://biostrap.com/
                    Shmoody: Mood & Habit Tracker
                    https://www.shmoody.com/
                    https://play.google.com/store/apps/details?id=com.yc14ec100daa.www&hl=en&gl=US
                    https://apps.apple.com/us/app/shmoody-mood-habit-tracker/id1534196157
                    Rx Longevity: Your optimal health, without pain.
                    https://rx-longevity.com/
                    https://play.google.com/store/apps/details?id=com.heartsradiant.rosita&hl=en&gl=US&pli=1
                    https://apps.apple.com/es/app/rosita-longevity-salud-60a%C3%B1os/id1535692117?mt=8
                    Spiritual Me®: Meditation App
                    https://spiritualme.com/
                    https://play.google.com/store/apps/details?id=com.spiritualmeapp.masters
                    https://apps.apple.com/us/app/spiritual-me-meditation-app/id985365789
                    HeadHelp: Self Care & Vent
                    https://www.headhelp.io/
                    https://play.google.com/store/apps/details?id=com.helponymous.helponymous&hl=en&gl=US
                    https://apps.apple.com/us/app/headhelp-self-care-vent/id1477936130
                    Kindly review with your team and feel free to let me know in case of any queries or concerns. Looking forward to hearing your thoughts.

                    Best Regards,
"""