---
entity_id: "protein.P21179"
entity_type: "protein"
name: "katE"
source_database: "UniProt"
source_id: "P21179"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "katE b1732 JW1721"
---

# katE

`protein.P21179`

## Static

- Type: `protein`
- Source: `UniProt:P21179`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Decomposes hydrogen peroxide into water and oxygen; serves to protect cells from the toxic effects of hydrogen peroxide. There are two distinct catalases in E. coli. The KatE enzyme is the monofunctional catalase HPII. A bifunctional catalase, HPI, is encoded by katG . Aerobically grown E. coli produce sufficient endogenous H2O2 to cause toxic levels of DNA damage via the Fenton reaction ; endogenously produced H2O2 is primarily scavenged by a third enzyme, CPLX0-245, while catalase is the primary scavenger at high H2O2 concentrations . While most heme proteins contain PROTOHEME as the prosthetic group, HPII contains a unique cofactor, HEME_D. It has been suggested that heme d is formed in a reaction catalyzed by HPII itself. Based on this model, HPII first binds protoheme, which is subsequently hydroxylated by HPII utilizing one of the first H2O2 substrate molecules . Later work has supported this theory. While HPII from aerobically grown E. coli contains heme d, HPII purified from microaerobic or anaerobic cultures contains a mixture of heme d and PROTOHEME. The protoheme of HPII obtained from such cells can be converted into heme d by treatment of the purified enzyme with hydrogen peroxide. The His128 residue of HPII is required for this conversion . A number of crystal structures of wild type and mutant forms of KatE have been reported...

## Biological Role

Catalyzes hydrogen-peroxide:hydrogen-peroxide oxidoreductase (reaction.R00009), methanol:hydrogen-peroxide oxidoreductase (reaction.R00602). Component of catalase HPII (complex.ecocyc.HYDROPEROXIDII-CPLX).

## Enriched Pathways

- `eco00380` Tryptophan metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco04146` Peroxisome (KEGG)

## Annotation

FUNCTION: Decomposes hydrogen peroxide into water and oxygen; serves to protect cells from the toxic effects of hydrogen peroxide.

## Pathways

- `eco00380` Tryptophan metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco04146` Peroxisome (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00009|reaction.R00009]] `KEGG` `database` - via EC:1.11.1.6
- `catalyzes` --> [[reaction.R00602|reaction.R00602]] `KEGG` `database` - via EC:1.11.1.6
- `is_component_of` --> [[complex.ecocyc.HYDROPEROXIDII-CPLX|complex.ecocyc.HYDROPEROXIDII-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1732|gene.b1732]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21179`
- `KEGG:ecj:JW1721;eco:b1732;ecoc:C3026_09900;`
- `GeneID:946234;`
- `GO:GO:0004096; GO:0005506; GO:0005737; GO:0005829; GO:0006972; GO:0006974; GO:0006979; GO:0020037; GO:0042744; GO:0042802`
- `EC:1.11.1.6`

## Notes

Catalase HPII (EC 1.11.1.6) (Hydroxyperoxidase II)
