{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPNGR+foOIolX73Tsd7hjMp",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/CtHaru240224/git-basic-kadai/blob/main/%E3%83%AA%E3%82%B9%E3%83%88/%E3%83%87%E3%82%A3%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AA%E3%82%92%E4%BD%BF%E3%81%84%E3%81%93%E3%81%AA%E3%81%9D%E3%81%86.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TmsJl2RWm_jW",
        "outputId": "f2535ac5-f16a-4bd2-9001-03b23eca5237"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "水曜日は晴れです\n"
          ]
        }
      ],
      "source": [
        "array = [\"月曜日は晴れです\", \"火曜日は雨です\", \"水曜日は晴れです\", \"木曜日は晴れです\", \"金曜日は曇りです\", \"土曜日は曇りのち雨です\", \"日曜日は雷雨です\"]\n",
        "print(array[2])"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dictionary= {\"mon\": \"晴れ\", \"tue\": \"雨\", \"wed\": \"晴れ\", \"thu\": \"晴れ\", \"fri\": \"曇り\", \"sat\": \"曇のち雨\", \"sun\": \"雷雨\"}\n",
        "print(f\"水曜日は{dictionary['wed']}です\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yI2OudJhnHQ1",
        "outputId": "b9b2d98f-f839-4043-ca12-a80b203a113b"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "水曜日は晴れです\n"
          ]
        }
      ]
    }
  ]
}