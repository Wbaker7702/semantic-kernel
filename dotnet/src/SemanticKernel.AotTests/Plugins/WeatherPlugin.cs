// Copyright (c) Microsoft. All rights reserved.

using System.ComponentModel;
using Microsoft.SemanticKernel;

namespace SemanticKernel.AotTests.Plugins;
internal sealed class WeatherPlugin
{
    [KernelFunction]
    [Description("Get the current weather in a given location.")]
    public Weather GetCurrentWeather(Location location)
    {
        return location.City switch
        {
            "Boston" => new Weather { Temperature = 0.75, Condition = "rainy" },
            "London" => new Weather { Temperature = 0.75, Condition = "cloudy" },
            "Miami" => new Weather { Temperature = 0.75, Condition = "sunny" },
            "Tokyo" => new Weather { Temperature = 0.75, Condition = "sunny" },
            "Sydney" => new Weather { Temperature = 0.75, Condition = "sunny" },
            _ => new Weather { Temperature = 0.75, Condition = "snowing" }
        };
    }
}
