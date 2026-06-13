---
entity_id: "protein.P25526"
entity_type: "protein"
name: "gabD"
source_database: "UniProt"
source_id: "P25526"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gabD b2661 JW2636"
---

# gabD

`protein.P25526`

## Static

- Type: `protein`
- Source: `UniProt:P25526`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NADP(+)-dependent oxidation of succinate semialdehyde to succinate (PubMed:20174634). Thereby functions in a GABA degradation pathway that allows some E.coli strains to utilize GABA as a nitrogen source for growth (PubMed:7011797). Also catalyzes the conversion of glutarate semialdehyde to glutarate, as part of a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). {ECO:0000269|PubMed:20174634, ECO:0000269|PubMed:30498244, ECO:0000305|PubMed:7011797}.

## Biological Role

Catalyzes succinate-semialdehyde:NAD+ oxidoreductase (reaction.R00713), succinate-semialdehyde:NADP+ oxidoreductase (reaction.R00714), glutarate-semialdehyde:NAD+ oxidoreductase (reaction.R02401). Component of succinate-semialdehyde dehydrogenase (NADP+) GabD (complex.ecocyc.CPLX0-7688).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the NADP(+)-dependent oxidation of succinate semialdehyde to succinate (PubMed:20174634). Thereby functions in a GABA degradation pathway that allows some E.coli strains to utilize GABA as a nitrogen source for growth (PubMed:7011797). Also catalyzes the conversion of glutarate semialdehyde to glutarate, as part of a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). {ECO:0000269|PubMed:20174634, ECO:0000269|PubMed:30498244, ECO:0000305|PubMed:7011797}.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00713|reaction.R00713]] `KEGG` `database` - via EC:1.2.1.16
- `catalyzes` --> [[reaction.R00714|reaction.R00714]] `KEGG` `database` - via EC:1.2.1.16
- `catalyzes` --> [[reaction.R02401|reaction.R02401]] `KEGG` `database` - via EC:1.2.1.20
- `is_component_of` --> [[complex.ecocyc.CPLX0-7688|complex.ecocyc.CPLX0-7688]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2661|gene.b2661]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25526`
- `KEGG:ecj:JW2636;eco:b2661;`
- `GeneID:948060;`
- `GO:GO:0004777; GO:0005829; GO:0009013; GO:0009450; GO:0032991; GO:0036243; GO:0042802; GO:0050661; GO:0051289; GO:0102810; GO:1990748`
- `EC:1.2.1.-; 1.2.1.79`

## Notes

Succinate-semialdehyde dehydrogenase [NADP(+)] GabD (SSDH) (EC 1.2.1.79) (Glutarate-semialdehyde dehydrogenase) (EC 1.2.1.-)
