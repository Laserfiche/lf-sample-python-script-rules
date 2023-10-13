# Sample Laserfiche Python Rule script project

Sample Python scripts that can be invoked from Laserfiche workflow or business process.

Scripts are invoked by **Laserfiche Remote Agent** which is a service installed on a Windows PC for this purpose.

## Prerequisites

- [Python 3.6 or later](https://www.python.org/downloads/)
- [Visual Studio Code v1.80 or later](https://code.visualstudio.com/download)
- [A Laserfiche Cloud Account](https://www.laserfiche.com/signon/)
- [Creating a Python Script Documentation](https://doc.laserfiche.com/laserfiche.documentation/en-us/Default.htm#../Subsystems/ProcessAutomation/Content/Resources/Rules/pythonscript.htm?TocPath=Process%2520Automation%257CRules%257CGetting%2520Started%2520With%2520Scripts%257C_____2)

## Build and Test script

This project is using a mono-repo structure with multiple packages. Please refer to the documentation for more details.

- Clone this GIT repository
- Install: `pip install -r requirements.txt`
- Test: `pytest`

## Configure a remote agent
[Remote Agents Documentation](https://doc.laserfiche.com/laserfiche.documentation/en-us/Default.htm#../Subsystems/ProcessAutomation/Content/Resources/Integrations/Remote-Agents/Remote-Agents.htm?TocPath=Process%2520Automation%257CIntegrations%257CRemote%2520Agents%257C_____0)

## Sample Projects
- [Template Python Script](doc/template/readme.md)
- [Word Translator](doc/word_translator/readme.md)
 
## Deployment
 - Copy the whole repo into the remote agent folder
    - e.g., `C:\Program Files\Laserfiche\Server\RemoteAgent\ScriptRunner\Python\lf-sample-python-script-rules`
 - Add the remote agent location into the **PYTHONPATH**
   ```python
   import os
   os.environ['PYTHONPATH'] = r'C:\Program Files\Laserfiche\Server\RemoteAgent\ScriptRunner\Python\lf-sample-python-script-rules'
   ```
 - Install dependencies: `pip install -r requirements.txt`
