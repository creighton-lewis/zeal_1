set -x 
echo 
echo "Installing homebrew" 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo "Installing nikto" 
    brew install nikto 
echo "Installing msfconsole" 
    curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
    chmod 755 msfinstall && \
    ./msfinstall
echo "Installing rustscan"
brew install rustscan 
echo "Installing 
