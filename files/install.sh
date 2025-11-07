set -x 
echo "Installing nikto" 
    brew install nikto 
echo "Installing msfconsole" 
    curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
    chmod 755 msfinstall && \
    ./msfinstall
echo "Installing rustscan"
brew install rustscan 
echo "Installing 