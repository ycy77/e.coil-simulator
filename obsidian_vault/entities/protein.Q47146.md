---
entity_id: "protein.Q47146"
entity_type: "protein"
name: "fadE"
source_database: "UniProt"
source_id: "Q47146"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fadE yafH b0221 JW5020"
---

# fadE

`protein.Q47146`

## Static

- Type: `protein`
- Source: `UniProt:Q47146`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydrogenation of acyl-coenzymes A (acyl-CoAs) to 2-enoyl-CoAs, the first step of the beta-oxidation cycle of fatty acid degradation. Is required for E.coli to utilize dodecanoate or oleate as the sole carbon and energy source for growth. {ECO:0000269|PubMed:12057976}. Acyl-CoA dehydrogenase (FadE) catalyzes the first step in the degradation of fatty acids via the β-oxidation cycle . fadE mutants are unable to utilize oleate and other fatty acids as the sole source of carbon . The fadE62 allele is a single base deletion resulting in a frame shift mutation, and yafH can complement the phenotype of the fadE62 mutant strain . Expression of the enzymes involved in β-oxidation is normally induced by fatty acids of chain length 14 and longer . Regulation is at the transcriptional level and involves repression by FadR . OldE: "oleate degradation E"

## Biological Role

Catalyzes ACYLCOADEHYDROG-RXN (reaction.ecocyc.ACYLCOADEHYDROG-RXN), RXN-17775 (reaction.ecocyc.RXN-17775), RXN-17779 (reaction.ecocyc.RXN-17779), RXN-17783 (reaction.ecocyc.RXN-17783), RXN-17784 (reaction.ecocyc.RXN-17784), RXN-17788 (reaction.ecocyc.RXN-17788), RXN-17792 (reaction.ecocyc.RXN-17792), RXN-17796 (reaction.ecocyc.RXN-17796).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydrogenation of acyl-coenzymes A (acyl-CoAs) to 2-enoyl-CoAs, the first step of the beta-oxidation cycle of fatty acid degradation. Is required for E.coli to utilize dodecanoate or oleate as the sole carbon and energy source for growth. {ECO:0000269|PubMed:12057976}.

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.ecocyc.ACYLCOADEHYDROG-RXN|reaction.ecocyc.ACYLCOADEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17775|reaction.ecocyc.RXN-17775]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17779|reaction.ecocyc.RXN-17779]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17783|reaction.ecocyc.RXN-17783]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17784|reaction.ecocyc.RXN-17784]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17788|reaction.ecocyc.RXN-17788]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17792|reaction.ecocyc.RXN-17792]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17796|reaction.ecocyc.RXN-17796]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0221|gene.b0221]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47146`
- `KEGG:ecj:JW5020;eco:b0221;ecoc:C3026_01045;`
- `GeneID:949007;`
- `GO:GO:0003995; GO:0004466; GO:0005737; GO:0009062; GO:0033539; GO:0050660; GO:0070991`
- `EC:1.3.8.7; 1.3.8.8`

## Notes

Acyl-coenzyme A dehydrogenase (ACDH) (Acyl-CoA dehydrogenase) (EC 1.3.8.7) (EC 1.3.8.8)
