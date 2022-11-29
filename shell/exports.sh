export JAVA_HOME='/'
export MAVEN_HOME='/opt/apache-maven-3.8.6'
export GEM_HOME="$HOME/.gem"
export GOPATH="$HOME/.go"
export ANDROID_HOME="$HOME/Android/Sdk"

export SPRING_CLI_HOME="$DOTFILES_PATH/langs/java/spring-cli/spring-2.3.9.BUILD-SNAPSHOT/bin"

export FZF_DEFAULT_OPTS='
  --color=pointer:#ebdbb2,bg+:#3c3836,fg:#ebdbb2,fg+:#fbf1c7,hl:#8ec07c,info:#928374,header:#fb4934
  --reverse
'

export path=(
  "$HOME/bin"
  "$DOTLY_PATH/bin"
  "$DOTFILES_PATH/bin"
  "$JAVA_HOME/bin"
  "$MAVEN_HOME/bin"
  "$ANDROID_HOME"
  "$ANDROID_HOME/emulator"
  "$ANDROID_HOME/tools"
  "$ANDROID_HOME/tools/bin"
  "$ANDROID_HOME/platform-tools"
  "$SPRING_CLI_HOME"
  "$GEM_HOME/bin"
  "$GOPATH/bin"
  "$HOME/.cargo/bin"
  "/usr/local/opt/ruby/bin"
  "/usr/local/opt/python/libexec/bin"
  "/opt/homebrew/bin"
  "/usr/local/bin"
  "/usr/local/sbin"
  "/bin"
  "/usr/bin"
  "/usr/sbin"
  "/sbin"
  "/snap/bin"
  "$HOME/.local/bin"
)
