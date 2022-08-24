mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"hamza.yaakoubi1@esprit.tn\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml