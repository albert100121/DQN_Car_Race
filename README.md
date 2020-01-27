# Car Race with RL
For the environment:
- pygame=1.9.6
- tensorflow-gpu=1.12
- cuda=9.0
- cudnn=7.6.5
- opencv
- PIL=7.0.0

[pip install pygame](https://pypi.org/project/pygame/)
[conda install -c anaconda pillow](https://anaconda.org/anaconda/)
[conda install -c conda-forge opencv](https://anaconda.org/conda-forge/opencv)
for quick install of environment
**Windows**
```
conda create --name ENV_NAME python=3.6.10
activate ENV_NAME
conda install --file requirement.txt
```
**Linux**
```
conda create --name ENV_NAME python=3.6.10
conda activate ENV_NAME
conda install --file re_linux.txt
```

For installation on tensorflow-gpu on windows with MX150
[tf-windows-MX150](https://medium.com/@johnnyliao/%E5%9C%A8win10%E4%B8%8A%E5%AE%89%E8%A3%9Dcuda-toolkit-cudnn-tensorflow-gpu-1-12%E4%BB%A5%E4%B8%8B%E5%8F%8A1-13%E4%BB%A5%E4%B8%8A-%E7%9A%84%E5%AE%89%E8%A3%9D%E7%B6%93%E9%A9%97%E5%88%86%E4%BA%AB-c792953b316f)
[windows-gpu-driver-check-Method2](https://www.drivereasy.com/knowledge/how-to-check-nvidia-driver-version-easily/) 
My gpu driver version: 398.35