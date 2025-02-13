// Initialize Firebase
const firebaseConfig = {
    apiKey: "{{ config.FIREBASE_API_KEY }}",
    authDomain: "{{ config.FIREBASE_AUTH_DOMAIN }}",
    projectId: "{{ config.FIREBASE_PROJECT_ID }}",
};


firebase.initializeApp(firebaseConfig);

// Firebase UI setup
const ui = new firebaseui.auth.AuthUI(firebase.auth());
ui.start('#firebase-auth-container', {
    signInOptions: [
        firebase.auth.EmailAuthProvider.PROVIDER_ID
    ],
    callbacks: {
        signInSuccessWithAuthResult: function(authResult, redirectUrl) {
            window.location.href = "/dashboard";
            return false;
        }
    }
});