---
entity_id: "protein.P52073"
entity_type: "protein"
name: "glcE"
source_database: "UniProt"
source_id: "P52073"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2689218}. Note=Glycolate oxidoreductase activity was shown to be firmly associated with the cytoplasmic membranes. {ECO:0000269|PubMed:2689218}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glcE gox yghL b4468 JW5487"
---

# glcE

`protein.P52073`

## Static

- Type: `protein`
- Source: `UniProt:P52073`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2689218}. Note=Glycolate oxidoreductase activity was shown to be firmly associated with the cytoplasmic membranes. {ECO:0000269|PubMed:2689218}.

## Enriched Summary

FUNCTION: Component of a complex that catalyzes the oxidation of glycolate to glyoxylate (PubMed:4557653, PubMed:8606183). Is required for E.coli to grow on glycolate as a sole source of carbon (PubMed:8606183). Is also able to oxidize D-lactate ((R)-lactate) with a similar rate (PubMed:4557653). Does not link directly to O(2), and 2,6-dichloroindophenol (DCIP) and phenazine methosulfate (PMS) can act as artificial electron acceptors in vitro, but the physiological molecule that functions as a primary electron acceptor during glycolate oxidation is unknown (PubMed:4557653). {ECO:0000269|PubMed:4557653, ECO:0000269|PubMed:8606183}. GlcE is predicted to contain a flavin-binding domain . A glcE insertion mutant lacks glycolate dehydrogenase activity . GlcE: "glycolate utilization E"

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

- `encodes` <-- [[gene.b4468|gene.b4468]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52073`
- `KEGG:ecj:JW5487;eco:b4468;ecoc:C3026_16295;`
- `GeneID:2847718;`
- `GO:GO:0005886; GO:0019154; GO:0046296; GO:0047809; GO:0071949`
- `EC:1.1.99.14`

## Notes

Glycolate oxidase subunit GlcE (EC 1.1.99.14) (Glycolate dehydrogenase subunit GlcE)
