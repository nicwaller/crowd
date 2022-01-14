import json
import os
from time import sleep
from typing import List, Optional

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
from slack_sdk.models.attachments import Attachment

app = App(token=os.environ["SLACK_BOT_TOKEN"])


class Persona:
    def __init__(self, username: str, *, icon_emoji: Optional[str] = None, icon_url: Optional[str] = None):
        self.username = username
        self.icon_emoji = icon_emoji
        self.icon_url = icon_url


# icon_emoji=':white_check_mark:',
# icon_emoji=':person_frowning:',
# icon_emoji=':person_with_headscarf:',
# icon_emoji=':person_with_blond_hair:',
# icon_emoji=':bald_person:',
# icon_emoji=':bearded_person:',


class Message:
    def __init__(self, wait: float, pers: Persona, text: str):
        self.wait = wait
        self.pers = Persona
        self.text = text
        # For some reason, copying the entire Persona object here does not work. Weird?!
        self.icon_url = pers.icon_url
        self.icon_emoji = pers.icon_emoji
        self.username = pers.username


class Scene:
    title: str
    key: str
    messages: List[Message]

    def __init__(self, key: str, title: str, messages: List[Message]):
        self.key = key
        self.title = title
        self.messages = messages




Neo = Persona('Neo', icon_url='https://nicwaller-public.s3-us-west-2.amazonaws.com/personas/neo_48.jpg')
Morpheus = Persona('Morpheus', icon_url='https://nicwaller-public.s3-us-west-2.amazonaws.com/personas/morpheus_48px.jpg')
TheMatrix = Scene("the-matrix", "The Matrix (1999)", [
    Message(0, Morpheus, "I imagine that right now, you're feeling a bit like Alice. Hmm? Tumbling down the rabbit hole?"),
    Message(4, Neo, "You could say that."),
    Message(3, Morpheus, "I see it in your eyes. You have the look of a man who accepts what he sees because he is expecting to wake up."),
    Message(3, Morpheus, "Ironically, that's not far from the truth. Do you believe in fate, Neo?"),
    Message(2, Neo, "No."),
    Message(2, Morpheus, "Why not?"),
    Message(3.5, Neo, "Because I don't like the idea that I'm not in control of my life."),
    Message(4, Morpheus, "I know *exactly* what you mean. Let me tell you why you're here."),
    Message(4, Morpheus, "You're here because you know something. What you know you can't explain, but you feel it. You've felt it your entire life, that there's something wrong with the world."),
    Message(5, Morpheus, "You don't know what it is, but it's there, like a splinter in your mind, driving you mad. It is this feeling that has brought you to me. Do you know what I'm talking about?"),
    Message(7, Neo, "The Matrix."),
    Message(4, Morpheus, "Do you want to know what it is?"),
    Message(2.5, Neo, "Yes."),
    Message(3, Morpheus, "The Matrix is everywhere. It is all around us. Even now, in this very room."),
    Message(5, Morpheus, "You can see it when you look out your window or when you turn on your television. You can feel it when you go to work... when you go to church... when you pay your taxes."),
    Message(4, Morpheus, "It is the world that has been pulled over your eyes to blind you from the truth."),
    Message(3, Neo, "What truth?"),
    Message(7, Morpheus, "That you are a slave, Neo. Like everyone else you were born into bondage. Into a prison that you cannot taste or see or touch. A prison for your mind."),
])

HarryPotter = Persona('Harry', icon_url='https://nicwaller-public.s3-us-west-2.amazonaws.com/personas/harrypotter.jpg')
RonWeasley = Persona('Ron', icon_url='https://nicwaller-public.s3-us-west-2.amazonaws.com/personas/ronweasley.jpg')
Hermione = Persona('Hermione', icon_url='https://nicwaller-public.s3-us-west-2.amazonaws.com/personas/hermione_48.jpg')
ChessQueen = Persona('♛', icon_url='https://nicwaller-public.s3-us-west-2.amazonaws.com/personas/HPChessQueen.jpg')

HarryPotterChessGame = Scene("harry-potter-1", "Harry Potter and the Philosopher's Stone (2001)", [
    Message(0, HarryPotter, "Wait a minute!"),
    Message(2, RonWeasley, "You see it, don't you, Harry?"),
    Message(2, RonWeasley, "Once I make my move, the Queen will take me..."),
    Message(2, RonWeasley, "Then you're free to check the King."),
    Message(2, HarryPotter, "No. Ron, NO!"),
    Message(2, Hermione, "What is it?"),
    Message(3, HarryPotter, "He's going to sacrifice himself."),
    Message(2, Hermione, "No, you can't!"),
    Message(2, Hermione, "There must be another way!"),
    Message(3.5, RonWeasley, "Do you want to stop Snape from getting that stone or not?"),
    Message(1.75, Hermione, ":neutral_face:"),  # 😐
    Message(4, RonWeasley, "Harry, it's you that has to go on, I *know* it."),
    Message(2, RonWeasley, "Not me, not Hermione, *YOU*."),
    Message(2, HarryPotter, ":cold_sweat:"),  # 😰
    Message(1.5, RonWeasley, ":grimacing: Knight to H3..."),  # 😬
    Message(1.5, RonWeasley, "Check."),
    Message(1, ChessQueen, "👀"),
    Message(1, ChessQueen, "https://nicwaller-public.s3-us-west-2.amazonaws.com/personas/QueenSwordHorse.jpg"),
    Message(2.5, RonWeasley, "🤯 😵"),
    Message(1.75, Hermione, "RON!"),
    Message(0.5, Hermione, ":woman-running:"),
    Message(0.5, HarryPotter, "NO! :raised_hand_with_fingers_splayed:"),
    Message(1.25, HarryPotter, "DON'T MOVE!"),
    Message(3, HarryPotter, "Don't forget - we're still playing."),
    Message(4, HarryPotter, "CHECKMATE."),
])

Karen = Persona('Karen', icon_url='https://nicwaller-public.s3-us-west-2.amazonaws.com/personas/mean_girls_karen.jpg')
Gretchen = Persona('Gretchen', icon_url='https://nicwaller-public.s3-us-west-2.amazonaws.com/personas/mean_girls_gretchen.jpg')
MeanGirlsCousins = Scene('mean-girls', "Mean Girls (2004)", [
    Message(0, Karen, "You know who's looking fine tonight?"),
    Message(1, Karen, "Seth Mosakowski."),
    Message(2, Gretchen, "Okay, you did *not* just say that."),
    Message(2, Karen, "What?"),
    Message(2, Karen, "He's a good kisser."),
    Message(2, Gretchen, "He's your _cousin_."),
    Message(2.5, Karen, "Yeah, but he's my first cousin."),
    Message(1.25, Gretchen, "Right."),
    Message(1.5, Karen, "So, you have your cousins,"),
    Message(2.0, Karen, "and then you have your first cousins,"),
    Message(2.5, Karen, "and then you have your second cousins..."),
    Message(1.5, Gretchen, "No, honey, uh-uh."),
    Message(2.5, Karen, "That's not right, is it? :thinking_face:"),
    Message(1.5, Gretchen, "That is _so_ not right. :face_vomiting:"),
])


Gandalf = Persona('Gandalf', icon_url='https://nicwaller-public.s3-us-west-2.amazonaws.com/personas/gandalf.jpg')
Bilbo = Persona('Bilbo Baggins', icon_url='https://nicwaller-public.s3-us-west-2.amazonaws.com/personas/bilbo.jpg')
LOTR_LeaveTheRing = Scene('lotr-fellowship', "The Lord of the Rings: The Fellowship of the Ring (2001)", [
    Message(0, Gandalf, "I think you should leave the ring behind, Bilbo."),
    Message(2, Gandalf, "Is that so hard?"),
    Message(2, Bilbo, "Well, no."),
    Message(2, Bilbo, "...and yes. :anguished:"),
    Message(3, Bilbo, "Now it comes to it, I don't feel like parting with it. :angry:"),
    Message(2, Bilbo, "It's mine, I found it. It came to me! :rage:"),
    Message(2, Gandalf, "There's no need to get angry."),
    Message(2, Bilbo, "Well, if I'm angry, it's your fault. :triumph:"),
    # Message(0, Bilbo, "_...it's mine... my own... my precious..._"),
    Message(2, Bilbo, "...it's mine..."),
    Message(1.75, Bilbo, "_my own..._"),
    Message(1.5, Bilbo, "ᵐʸ ᵖʳᵉᶜᶦᵒᵘˢ"),
    Message(1, Gandalf, "Precious?"),
    Message(2, Gandalf, "It's been called that before, but not by you."),
    Message(2, Bilbo, "Oh, what business is it of yours what I do with my own things?"),
    Message(2, Gandalf, "I think you've had that ring quite long enough."),
    Message(2, Bilbo, "You want it for yourself!"),
    Message(1, Gandalf, "*𝐁𝐈𝐋𝐁𝐎 𝐁𝐀𝐆𝐆𝐈𝐍𝐒!*"),
    Message(2.5, Gandalf, "Do not take me for some conjuror of cheap tricks!"),
    Message(2.5, Gandalf, "I am not trying to rob you. I'm trying to help you."),
])

scenes: List[Scene] = [
    TheMatrix,
    HarryPotterChessGame,
    MeanGirlsCousins,
    LOTR_LeaveTheRing,
]


def spit(channel_id: str, conversation: List[Message]):
    for message in conversation:
        attachments = []
        sleep(message.wait)
        if message.text.endswith('.jpg'):
            attachments.append(Attachment(text='', fallback=message.text, image_url=message.text))
            message.text = ''
        app.client.chat_postMessage(
            text=message.text,
            channel=channel_id,
            # icon_emoji=message.icon_emoji,
            icon_url=message.icon_url,
            username=message.username,
            attachments=attachments,
            unfurl_links=False,
            unfurl_media=False,
        )


previous_scene_id: int = 0


# Add middleware / listeners here
# The echo command simply echoes on command
@app.command("/crowd")
def repeat_text(ack, respond, command):
    # Acknowledge command request
    ack()
    trigger_id = command['trigger_id']
    # respond("Starting dialogue...")
    # spit(command['channel_id'], LOTR_LeaveTheRing)
    # respond("Scene complete.")
    global previous_scene_id
    app.client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=trigger_id,
        # View payload
        view={
            "callback_id": "scene_select",
            "type": "modal",
            "title": {
                "type": "plain_text",
                "text": "Generate Dialogue",
                "emoji": True
            },
            "submit": {
                "type": "plain_text",
                "text": "Start Scene",
                "emoji": True
            },
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "input",
                    "block_id": "scene",
                    "element": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Pick a movie",
                            "emoji": False
                        },
                        "initial_option": {
                            "text": {
                                "type": "plain_text",
                                "text": scenes[previous_scene_id].title,
                                "emoji": False
                            },
                            "value": scenes[previous_scene_id].key
                        },
                        "options": [{
                            "text": {
                                "type": "plain_text",
                                "text": scene.title,
                                "emoji": False
                            },
                            "value": scene.key
                        } for scene in scenes],
                        "action_id": "scene"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Pick a movie",
                        "emoji": False
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Pick a channel*"
                    }
                },
                {
                    "type": "actions",
                    "block_id": "channel",
                    "elements": [
                        {
                            "type": "channels_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select a channel",
                                "emoji": False
                            },
                            "initial_channel": command['channel_id'],
                            "action_id": "channel"
                        }
                    ]
                },
                {
                    "type": "section",
                    "block_id": "delay",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Wait how long before starting scene?"
                    },
                    "accessory": {
                        "type": "static_select",
                        "initial_option": {
                            "text": {
                                "type": "plain_text",
                                "text": "1 second",
                                "emoji": True
                            },
                            "value": "1"
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "1 second",
                                    "emoji": True
                                },
                                "value": "1"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "5 seconds",
                                    "emoji": True
                                },
                                "value": "5"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "15 seconds",
                                    "emoji": True
                                },
                                "value": "15"
                            }
                        ],
                        "action_id": "delay"
                    }
                }
            ]
        }
    )


@app.view("scene_select")
def handle_view_events(ack, body, logger):
    ack()
    logger.info(body)
    view_response = body['view']['state']['values']
    scene_key = view_response['scene']['scene']['selected_option']['value']
    channel_id = view_response['channel']['channel']['selected_channel']
    delay = int(view_response['delay']['delay']['selected_option']['value'])
    global previous_scene_id
    (previous_scene_id, scene) = list(filter(lambda x: x[1].key == scene_key, enumerate(scenes)))[0]
    sleep(delay)
    spit(channel_id, scene.messages)


if __name__ == "__main__":
    # export SLACK_APP_TOKEN=xapp-***
    # export SLACK_BOT_TOKEN=xoxb-***
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
