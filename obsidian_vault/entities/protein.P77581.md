---
entity_id: "protein.P77581"
entity_type: "protein"
name: "astC"
source_database: "UniProt"
source_id: "P77581"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "astC argM cstC ydjW b1748 JW1737"
---

# astC

`protein.P77581`

## Static

- Type: `protein`
- Source: `UniProt:P77581`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transamination of N(2)-succinylornithine and alpha-ketoglutarate into N(2)-succinylglutamate semialdehyde and glutamate. Can also act as an acetylornithine aminotransferase. Is involved in the utilization of arginine as a nitrogen source, via the AST pathway, and also seems to play a role in ornithine catabolism (PubMed:9696779). {ECO:0000269|PubMed:9696779}. Succinylornithine transaminase (AstC) catalyzes the third reaction in the ammonia-producing arginine catabolic pathway, AST-PWY. The astC gene is 60% identical to EG10066 "argD", which encodes the arginine-repressible N-acetylornithine aminotransferase . Four enzymes, ArgD, AstC, GabT, and PuuE, show some level of N-acetylornithine aminotransferase (ACOAT) activity involved in arginine biosynthesis. On minimal medium lacking arginine, single argD or astC mutants have subtle growth defects, and an argD astC double mutant has a slower doubling time than wild type. An argD astC gabT triple mutant does not grow on medium lacking arginine. Accumulation of suppressor mutations eventually allows growth of the triple mutant; an additional deletion of puuE eliminates this effect...

## Biological Role

Component of succinylornithine transaminase (complex.ecocyc.SUCCORNTRANSAM-CPLX).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the transamination of N(2)-succinylornithine and alpha-ketoglutarate into N(2)-succinylglutamate semialdehyde and glutamate. Can also act as an acetylornithine aminotransferase. Is involved in the utilization of arginine as a nitrogen source, via the AST pathway, and also seems to play a role in ornithine catabolism (PubMed:9696779). {ECO:0000269|PubMed:9696779}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.SUCCORNTRANSAM-CPLX|complex.ecocyc.SUCCORNTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1748|gene.b1748]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77581`
- `KEGG:ecj:JW1737;eco:b1748;ecoc:C3026_09985;`
- `GeneID:75203054;946255;`
- `GO:GO:0003992; GO:0006527; GO:0006593; GO:0019544; GO:0019545; GO:0030170; GO:0042450; GO:0042802; GO:0043825`
- `EC:2.6.1.81`

## Notes

Succinylornithine transaminase (SOAT) (EC 2.6.1.81) (Carbon starvation protein C) (Succinylornithine aminotransferase)
