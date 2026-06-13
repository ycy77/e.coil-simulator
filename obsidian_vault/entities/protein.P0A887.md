---
entity_id: "protein.P0A887"
entity_type: "protein"
name: "ubiE"
source_database: "UniProt"
source_id: "P0A887"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:30686758}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiE yigO b3833 JW5581"
---

# ubiE

`protein.P0A887`

## Static

- Type: `protein`
- Source: `UniProt:P0A887`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:30686758}.

## Enriched Summary

FUNCTION: Methyltransferase required for the conversion of demethylmenaquinol (DMKH2) to menaquinol (MKH2) and the conversion of 2-polyprenyl-6-methoxy-1,4-benzoquinol (DDMQH2) to 2-polyprenyl-3-methyl-6-methoxy-1,4-benzoquinol (DMQH2) (PubMed:9045837). In vitro, can use demethylphylloquinol, an intermediate in the biosynthesis of phylloquinone (vitamin K1) in plants and cyanobacteria (PubMed:26023160). {ECO:0000269|PubMed:26023160, ECO:0000269|PubMed:9045837}. UbiE is a C-methyltransferase that catalyzes reactions in both ubiquinone (Q) and menaquinone (MK) biosynthesis. Q biosynthesis and MK biosynthesis diverge after the formation of chorismate and the pathways proceed independently except for the C methylation step. In Q biosynthesis, UbiE catalyzes the conversion of 2-octaprenyl-6-methoxy-1,4-benzoquinone to 2-octaprenyl-3-methyl-6-methoxy-1,4-benzoquinone. In MK biosynthesis, UbiE catalyzes the conversion of demethylmenaquinone to menaquinone . UbiE localizes to both soluble and membrane fractions. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol . A ubiE mutant accumulates 2-octaprenyl-6-methoxy-1,4-benzoquinone, an intermediate in ubiquinone (Q) biosynthesis , and is unable to convert demethylmenaquinone (DMK) to menaquinone (MK), accumulating DMK...

## Biological Role

Catalyzes 2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN (reaction.ecocyc.2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN), ADOMET-DMK-METHYLTRANSFER-RXN (reaction.ecocyc.ADOMET-DMK-METHYLTRANSFER-RXN). Component of Ubi complex (complex.ecocyc.CPLX0-8301).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Methyltransferase required for the conversion of demethylmenaquinol (DMKH2) to menaquinol (MKH2) and the conversion of 2-polyprenyl-6-methoxy-1,4-benzoquinol (DDMQH2) to 2-polyprenyl-3-methyl-6-methoxy-1,4-benzoquinol (DMQH2) (PubMed:9045837). In vitro, can use demethylphylloquinol, an intermediate in the biosynthesis of phylloquinone (vitamin K1) in plants and cyanobacteria (PubMed:26023160). {ECO:0000269|PubMed:26023160, ECO:0000269|PubMed:9045837}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN|reaction.ecocyc.2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ADOMET-DMK-METHYLTRANSFER-RXN|reaction.ecocyc.ADOMET-DMK-METHYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-8301|complex.ecocyc.CPLX0-8301]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3833|gene.b3833]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A887`
- `KEGG:ecj:JW5581;eco:b3833;ecoc:C3026_20740;`
- `GeneID:86861938;93778102;948926;`
- `GO:GO:0005737; GO:0006744; GO:0008425; GO:0009060; GO:0009234; GO:0032259; GO:0043770; GO:0110142`
- `EC:2.1.1.163; 2.1.1.201`

## Notes

Ubiquinone/menaquinone biosynthesis C-methyltransferase UbiE (EC 2.1.1.163) (EC 2.1.1.201) (2-methoxy-6-polyprenyl-1,4-benzoquinol methylase) (Demethylmenaquinone methyltransferase)
