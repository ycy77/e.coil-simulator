---
entity_id: "protein.P52074"
entity_type: "protein"
name: "glcF"
source_database: "UniProt"
source_id: "P52074"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2689218, ECO:0000305|PubMed:8606183}. Note=Glycolate oxidoreductase activity was shown to be firmly associated with the cytoplasmic membranes (PubMed:2689218). And the GlcF subunit itself could only be detected in the membrane fraction (PubMed:8606183). {ECO:0000269|PubMed:2689218, ECO:0000269|PubMed:8606183}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glcF gox yghL b4467 JW5486"
---

# glcF

`protein.P52074`

## Static

- Type: `protein`
- Source: `UniProt:P52074`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2689218, ECO:0000305|PubMed:8606183}. Note=Glycolate oxidoreductase activity was shown to be firmly associated with the cytoplasmic membranes (PubMed:2689218). And the GlcF subunit itself could only be detected in the membrane fraction (PubMed:8606183). {ECO:0000269|PubMed:2689218, ECO:0000269|PubMed:8606183}.

## Enriched Summary

FUNCTION: Component of a complex that catalyzes the oxidation of glycolate to glyoxylate (PubMed:4557653, PubMed:8606183). Is required for E.coli to grow on glycolate as a sole source of carbon (PubMed:8606183). Is also able to oxidize D-lactate ((R)-lactate) with a similar rate (PubMed:4557653). Does not link directly to O(2), and 2,6-dichloroindophenol (DCIP) and phenazine methosulfate (PMS) can act as artificial electron acceptors in vitro, but the physiological molecule that functions as a primary electron acceptor during glycolate oxidation is unknown (PubMed:4557653). {ECO:0000269|PubMed:4557653, ECO:0000269|PubMed:8606183}. GlcF is similar to iron-sulfur proteins and could only be detected as a membrane-associated protein . A glcF insertion mutant lacks glycolate dehydrogenase activity . glcF expression is increased in a mutant with enhanced butanol tolerance; overexpression of glcF in an otherwise wild-type background improves growth in the presence of butanol slightly . GlcF: "glycolate utilization F"

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

- `encodes` <-- [[gene.b4467|gene.b4467]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52074`
- `KEGG:ecj:JW5486;eco:b4467;ecoc:C3026_16290;`
- `GeneID:2847717;75173103;`
- `GO:GO:0005886; GO:0019154; GO:0046296; GO:0046872; GO:0047809; GO:0051539`
- `EC:1.1.99.14`

## Notes

Glycolate oxidase iron-sulfur subunit (EC 1.1.99.14) (Glycolate dehydrogenase subunit GlcF) (Glycolate oxidase subunit GlcF)
