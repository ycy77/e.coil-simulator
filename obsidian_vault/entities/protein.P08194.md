---
entity_id: "protein.P08194"
entity_type: "protein"
name: "glpT"
source_database: "UniProt"
source_id: "P08194"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glpT b2240 JW2234"
---

# glpT

`protein.P08194`

## Static

- Type: `protein`
- Source: `UniProt:P08194`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Responsible for glycerol-3-phosphate uptake. GlpT is the major E. coli uptake system for sn-glycerol 3-phosphate, and this transporter belongs to the Major Facilitator Superfamily (MFS) of transporters . Uptake of sn-glycerol 3-phosphate via the GlpT transporter leads to the simultaneous counterflow of inorganic phosphate from the cell . GlpT also catalyzes a reversible phosphate:phosphate exchange . Both sn-glycerol 3-phosphate:phosphate and phosphate:phosphate exchange activities were observed in GlpT-reconstituted proteoliposomes . Using phosphate-loaded proteoliposomes, the Km for the transport of sn-glycerol 3-phosphate via GlpT was estimated to be near 20 μM and the Vmax was 130 nmol min-1 mg-1 . GlpT has been crystallized and the structure has been determined by X-ray crystallography to a resolution of 3.3 Å . The functional form of GlpT is the monomer . GlpT exhibits a rocker-switch mechanism of transport although transport via a 'tilted' mechanism has also been proposed . Experiments using PhoA/LacZ fusions revealed GlpT has twelve transmembrane segments . The residues involved in binding the substrate have been identified as well as the substrate binding mechanism which involves protonation of a histidine residue at the binding site. It has been suggested that translocation of the substrate occurs as a result of salt bridge formation and disruption...

## Biological Role

Catalyzes glycerol-3-phosphate:phosphate antiport (reaction.ecocyc.TRANS-RXN-22). Transports sn-Glycerol 3-phosphate (molecule.C00093).

## Annotation

FUNCTION: Responsible for glycerol-3-phosphate uptake.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-22|reaction.ecocyc.TRANS-RXN-22]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2240|gene.b2240]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08194`
- `KEGG:ecj:JW2234;eco:b2240;ecoc:C3026_12515;`
- `GeneID:946704;`
- `GO:GO:0005886; GO:0006071; GO:0015169; GO:0015315; GO:0015527; GO:0015760; GO:0015793; GO:0015794; GO:0035435; GO:0061513`

## Notes

Glycerol-3-phosphate transporter (G-3-P transporter) (G-3-P permease)
