# Contributor Guide

## Commit Messages

The subject line/first line of a commit description should be an action.
Instead of being passive - such as "changes x to y" - it should be active,
as in "change x to y".

The beginning paragraphs of the commit message should describe what the
patch does. They should describe everything that was changed, the benefits,
the potential drawbacks, and the reasoning for making the change.

For each bug fixed/issue addressed, a line saying "Fixes: #BUGNUMBER"
should be used. For instance, if issues 31 and 35 are being resolved:

```
Fixes: #31
Fixes: #35
```

If someone else wrote the patch with you, credit them as such:

```
Co-developed-by: Person's Name <name@email.tld>
```

If someone reviewed the patch, use `Reviewed-by`; if they just
acknowledged it exists, use `Acked-by`:

```
Reviewed-by: Reviewer's Name <name@email.tld>
Acked-by: Acker's Name <name@email.tld>
```

> To use Reviewed-by, the person must have given their consent for you
> to use it. They can do this by replying to a patch with the Reviewed-by
> line you would use.

If you want to make sure someone sees the patch, use Cc:

```
Cc: Important Person <name@email.tld>
```

If someone else tested the patch for you:

```
Tested-by: Tester's Name <name@email.tld>
```

If the patch came from someone's suggestion:

```
Suggested-by: Suggester's Name <name@email.tld>
```

Finally, the last line of the patch should be a signoff:

```
Signed-off-by: Your Name <name@email.tld>
```

By using Signed-off-by, you are agreeing to the
[Developer's Certificate of Origin](https://developercertificate.org/).