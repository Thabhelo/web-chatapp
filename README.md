# web-chatapp
# Talladega Chat

Talladega Chat is a web-based chat application that enables real-time communication between users. With Talladega Chat, users can engage in instant messaging, create chat rooms, and enjoy a seamless chatting experience.

## Features

- **Real-time Messaging**: Communicate with other users in real-time, ensuring instant and responsive conversations.
- **User Authentication**: Secure user authentication system ensures that only registered users can access Talladega Chat.
- **Chat Rooms**: Create and join chat rooms to facilitate group conversations with specific topics or interests.
- **Customizable Profiles**: Personalize your profile by adding a profile picture and customizing your display name.
- **Message History**: Easily access and view your chat history, allowing you to review previous conversations.
- **Notifications**: Stay informed with notifications for new messages and activity in your chat rooms.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/thabhelo/talladega-chat.git
   ```

2. Install dependencies:

   ```bash
   cd talladega-chat
   npm install
   ```

3. Configure the environment variables:
   - Rename the `.env.example` file to `.env`.
   - Update the environment variables in the `.env` file with your own configuration (e.g., database credentials, API keys).

4. Start the development server:

   ```bash
   npm run dev
   ```

5. Open your web browser and visit `http://localhost:3000` to access Talladega Chat.

## Technologies Used

- **Frontend**: HTML, TailwindCSS, JavaScript
- **Backend**: Django - channels
- **Database**: DynamoDB
- **Real-time Communication**: Socket.io
- **Authentication**: JSON Web Tokens (JWT)

## Contributing

Contributions to Talladega Chat are welcome! If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your branch.
4. Submit a pull request with a detailed description of your changes.

## License

Talladega Chat is released under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements

- The project structure and design were inspired by various open-source chat applications.
- Special thanks to the contributors and the open-source community for their valuable contributions and support.
- SPecial thanks to @codewithstein for valuable advices and tutoring me on Django

## Contact

For any questions or inquiries, please contact the Talladega Chat team at thabhelo.duve@talladega.edu.
