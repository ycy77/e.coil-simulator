---
entity_id: "protein.P0AEV9"
entity_type: "protein"
name: "hycI"
source_database: "UniProt"
source_id: "P0AEV9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hycI b2717 JW2687"
---

# hycI

`protein.P0AEV9`

## Static

- Type: `protein`
- Source: `UniProt:P0AEV9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Protease involved in the C-terminal processing of HycE, the large subunit of hydrogenase 3. {ECO:0000269|PubMed:10727938}. HycI is an endopeptidase that belongs to the M52 peptidase family; it cleaves 32 amino acids off the carboxy-terminus of HYCELARGE-MONOMER HycE, modifying it into its final form as the large subunit of hydrogenase 3 . The substrate HycE must have nickel bound in its center for the processing step to take place . When nickel uptake is blocked, zinc can disrupt HycI proteolysis of HycE, possibly by binding in the nickel site of HycE . HycI shows a somewhat relaxed specificity for amino acid residues at the HycE cleavage site; however, HycI does not cleave a substrate where the C-terminal extension of HycE is swapped for that of HybC . The HycI homolog HyfK from Pectobacterium atrosepticum is able to process the E. coli HycE protein . A high resolution solution structure of the apo form of recombinant HycI was determined by nuclear magnetic resonance spectroscopy . In addition, recombinant HycI was crystallized in the presence of Ca2+ and its crystal structure was determined at 1.70 Å resolution. Three specific metal binding sites were identified that might be involved in the C-terminal cleavage of HycE . Mutation of conserved residues in HycI which match cadmium-binding residues in the related endopeptidase HybD reduces HycI protease activity...

## Biological Role

Catalyzes RXN-22655 (reaction.ecocyc.RXN-22655).

## Annotation

FUNCTION: Protease involved in the C-terminal processing of HycE, the large subunit of hydrogenase 3. {ECO:0000269|PubMed:10727938}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-22655|reaction.ecocyc.RXN-22655]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2717|gene.b2717]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEV9`
- `KEGG:ecj:JW2687;eco:b2717;ecoc:C3026_14950;`
- `GeneID:93779291;947428;`
- `GO:GO:0004175; GO:0004190; GO:0008047; GO:0016485; GO:0046872`
- `EC:3.4.23.51`

## Notes

Hydrogenase 3 maturation protease (EC 3.4.23.51) (HycI protease)
