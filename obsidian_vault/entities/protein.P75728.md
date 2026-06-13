---
entity_id: "protein.P75728"
entity_type: "protein"
name: "ubiF"
source_database: "UniProt"
source_id: "P75728"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:30686758}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiF yleB b0662 JW0659"
---

# ubiF

`protein.P75728`

## Static

- Type: `protein`
- Source: `UniProt:P75728`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:30686758}.

## Enriched Summary

FUNCTION: Catalyzes the hydroxylation of 2-octaprenyl-3-methyl-6-methoxy-1,4-benzoquinol during ubiquinone biosynthesis. {ECO:0000269|PubMed:10802164}. 2-Octaprenyl-3-methyl-6-methoxy-1,4-benzoquinol hydroxylase catalyzes the hydroxylation of C-5 of the benzene moiety in the biosynthesis of ubiquinone. The enzyme has not been characterized biochemically. UbiF is a component of the Ubi complex metabolon . UbiF predominantly localizes to the cytosol. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol . A ubiF mutant accumulates 2-octaprenyl-3-methyl-6-methoxy-1,4-benzoquinone (MMQ-8) and has only a slight growth defect . MMQ-8 itself can function fairly efficiently (~50%) as an electron carrier in the NADH, D-lactate, and glycerol-3-phosphate dehydrogenase systems, but only poorly for the oxidation of succinate . A ubiF mutant is unable to grow on succinate as the sole source of carbon and energy . ubiF mutants have reduced capacity for uptake of aminoglycoside antibiotics and are resistant to phleomycin, bleomycin, and heat inactivation . Mutants in ubiF, ubiH, ubiX, ubiG, and ubiE from the Keio K-12 mutant collection showed elevated resistance to the broad-spectrum antibiotic D-cycloserine (DCS) when grown in complex media, suggesting that they may be involved in DCS sensitivity...

## Biological Role

Catalyzes 5-methoxy-2-methyl-3-(all-trans-polyprenyl)benzene-1,4-diol,acceptor:oxygen oxidoreductase (5-hydroxylating) (reaction.R12067), OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN (reaction.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN). Component of Ubi complex (complex.ecocyc.CPLX0-8301).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the hydroxylation of 2-octaprenyl-3-methyl-6-methoxy-1,4-benzoquinol during ubiquinone biosynthesis. {ECO:0000269|PubMed:10802164}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R12067|reaction.R12067]] `KEGG` `database` - via EC:1.14.99.60
- `catalyzes` --> [[reaction.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN|reaction.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-8301|complex.ecocyc.CPLX0-8301]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0662|gene.b0662]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75728`
- `KEGG:ecj:JW0659;eco:b0662;ecoc:C3026_03310;`
- `GeneID:945261;`
- `GO:GO:0005737; GO:0006744; GO:0008682; GO:0016705; GO:0071949; GO:0110142`
- `EC:1.14.99.60`

## Notes

3-demethoxyubiquinol 3-hydroxylase (EC 1.14.99.60) (2-octaprenyl-3-methyl-6-methoxy-1,4-benzoquinol hydroxylase)
