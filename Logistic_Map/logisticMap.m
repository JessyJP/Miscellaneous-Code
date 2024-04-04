function x = logisticMap(r, x0, n)
    % r: growth rate parameter
    % x0: initial population ratio (between 0 and 1)
    % n: number of generations

    % Preallocate the array for performance
    x = zeros(1, n);
    x(1) = x0; % Set initial value

    for i = 2:n
        % Calculate next generation
        x(i) = r * x(i-1) * (1 - x(i-1));
    end
end
