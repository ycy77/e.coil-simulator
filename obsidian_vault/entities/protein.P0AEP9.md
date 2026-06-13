---
entity_id: "protein.P0AEP9"
entity_type: "protein"
name: "glcD"
source_database: "UniProt"
source_id: "P0AEP9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2689218}. Note=Glycolate oxidoreductase activity was shown to be firmly associated with the cytoplasmic membranes. {ECO:0000269|PubMed:2689218}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glcD gox yghM b2979 JW2946"
---

# glcD

`protein.P0AEP9`

## Static

- Type: `protein`
- Source: `UniProt:P0AEP9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2689218}. Note=Glycolate oxidoreductase activity was shown to be firmly associated with the cytoplasmic membranes. {ECO:0000269|PubMed:2689218}.

## Enriched Summary

FUNCTION: Component of a complex that catalyzes the oxidation of glycolate to glyoxylate (PubMed:4557653, PubMed:8606183). Is required for E.coli to grow on glycolate as a sole source of carbon (PubMed:8606183). Is also able to oxidize D-lactate ((R)-lactate) with a similar rate (PubMed:4557653). Does not link directly to O(2), and 2,6-dichloroindophenol (DCIP) and phenazine methosulfate (PMS) can act as artificial electron acceptors in vitro, but the physiological molecule that functions as a primary electron acceptor during glycolate oxidation is unknown (PubMed:4557653). {ECO:0000269|PubMed:4557653, ECO:0000269|PubMed:8606183}. GlcD is predicted to contain a flavin-binding domain . A glcD insertion mutant lacks glycolate dehydrogenase activity . GlcD: "glycolate utilization D"

## Biological Role

Catalyzes glycolate:acceptor 2-oxidoreductase (reaction.R00476). Component of glycolate dehydrogenase (complex.ecocyc.CPLX0-7458).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Component of a complex that catalyzes the oxidation of glycolate to glyoxylate (PubMed:4557653, PubMed:8606183). Is required for E.coli to grow on glycolate as a sole source of carbon (PubMed:8606183). Is also able to oxidize D-lactate ((R)-lactate) with a similar rate (PubMed:4557653). Does not link directly to O(2), and 2,6-dichloroindophenol (DCIP) and phenazine methosulfate (PMS) can act as artificial electron acceptors in vitro, but the physiological molecule that functions as a primary electron acceptor during glycolate oxidation is unknown (PubMed:4557653). {ECO:0000269|PubMed:4557653, ECO:0000269|PubMed:8606183}.

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00476|reaction.R00476]] `KEGG` `database` - via EC:1.1.99.14
- `is_component_of` --> [[complex.ecocyc.CPLX0-7458|complex.ecocyc.CPLX0-7458]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2979|gene.b2979]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEP9`
- `KEGG:ecj:JW2946;eco:b2979;ecoc:C3026_16300;`
- `GeneID:75205189;947353;`
- `GO:GO:0003973; GO:0005886; GO:0006974; GO:0009339; GO:0019154; GO:0046296; GO:0047809; GO:0071949`
- `EC:1.1.99.14`

## Notes

Glycolate oxidase subunit GlcD (EC 1.1.99.14) (Glycolate dehydrogenase subunit GlcD)
