---
entity_id: "protein.P31678"
entity_type: "protein"
name: "otsB"
source_database: "UniProt"
source_id: "P31678"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "otsB b1897 JW1886"
---

# otsB

`protein.P31678`

## Static

- Type: `protein`
- Source: `UniProt:P31678`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Removes the phosphate from trehalose 6-phosphate (Tre6P) to produce free trehalose. Also catalyzes the dephosphorylation of glucose-6-phosphate (Glu6P) and 2-deoxyglucose-6-phosphate (2dGlu6P). {ECO:0000269|PubMed:1310094, ECO:0000269|PubMed:16990279}. otsB encodes the biosynthetic trehalose-6-phosphate phosphatase, which belongs to the superfamily of haloacid dehalogenase (HAD)-like hydrolases . The phosphatase activity of OtsB was also found in a high-throughput screen of purified proteins . Accumulation of trehalose at low temperatures enhances cell viability . An otsBA double mutant is more sensitive than wild type to heat shock during stationary phase, but not during exponential growth . Expression of otsB is increased under osmotic stress and induced during the transition to stationary phase and by low temperature in a σS-dependent manner . Stability of otsBA mRNA is increased approximately 10-fold at 16°C compared to 37°C . Under nutrient-limiting conditions in an RpoS mutant strain background, an adaptive mutation that allows RpoS-independent transcription of otsBA arises spontaneously and increases fitness . OtsB: "osmoregulatory trehalose synthesis B" Reviews:

## Biological Role

Catalyzes TREHALOSEPHOSPHA-RXN (reaction.ecocyc.TREHALOSEPHOSPHA-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Removes the phosphate from trehalose 6-phosphate (Tre6P) to produce free trehalose. Also catalyzes the dephosphorylation of glucose-6-phosphate (Glu6P) and 2-deoxyglucose-6-phosphate (2dGlu6P). {ECO:0000269|PubMed:1310094, ECO:0000269|PubMed:16990279}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TREHALOSEPHOSPHA-RXN|reaction.ecocyc.TREHALOSEPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1897|gene.b1897]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31678`
- `KEGG:ecj:JW1886;eco:b1897;ecoc:C3026_10775;`
- `GeneID:93776200;946406;`
- `GO:GO:0000287; GO:0004805; GO:0005992; GO:0006970; GO:0070417`
- `EC:3.1.3.12`

## Notes

Trehalose-6-phosphate phosphatase (TPP) (EC 3.1.3.12) (Osmoregulatory trehalose synthesis protein B) (Trehalose 6-phosphate phosphatase) (Trehalose-phosphatase)
