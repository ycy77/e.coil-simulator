---
entity_id: "protein.P43329"
entity_type: "protein"
name: "hrpA"
source_database: "UniProt"
source_id: "P43329"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hrpA b1413 JW5905"
---

# hrpA

`protein.P43329`

## Static

- Type: `protein`
- Source: `UniProt:P43329`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Not yet known. HrpA belongs to the family of DEAH-box RNA helicases and has ATP-dependent 3'→5' RNA helicase activity . The helicase activity resides within the N-terminal 783 amino acids of HrpA, while the C-terminal region directly contacts the N-terminal region and appears to modulate its helicase activity . Crystal structures of apo-HrpA1-178, HrpA1-178 in complex with a ssRNA, and apo-HrpA1-178, D305A have been solved, showing that he enzyme undergoes large conformational changes upon RNA binding that are facilitated by alternative interdomain contacts involving the D305 residue. A K106A mutant within a conserved sequence motif of the RecA1-like domain of HrpA shows reduced ATPase activity. The "stacking triad" consisting of F655, P656, and F661 within the OB domain of HrpA is required for helicase activity . Further crystallization studies found functional N-terminal and C-terminal extensions. The N-terminal has an antiparallel helix-bundle domain (APHB) near the RecA-like domains that functions in ssDNA and ssRNA recognition and binding, and functions in RNA/RNA and RNA/DNA duplex unwinding. Co-crystals of the full Hrpa protein with various substrates also revealed its ability to bind DNA/RNA G-quadruplex (G4) and intercalated motif (i-motif) structures...

## Biological Role

Catalyzes RXN-24177 (reaction.ecocyc.RXN-24177).

## Annotation

FUNCTION: Not yet known.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-24177|reaction.ecocyc.RXN-24177]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1413|gene.b1413]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P43329`
- `KEGG:ecj:JW5905;eco:b1413;ecoc:C3026_08230;`
- `GeneID:948444;`
- `GO:GO:0003723; GO:0003724; GO:0004386; GO:0005524; GO:0009451; GO:0016887; GO:0034458`
- `EC:3.6.4.13`

## Notes

ATP-dependent RNA helicase HrpA (EC 3.6.4.13)
