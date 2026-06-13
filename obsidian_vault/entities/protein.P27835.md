---
entity_id: "protein.P27835"
entity_type: "protein"
name: "wzyE"
source_database: "UniProt"
source_id: "P27835"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01003, ECO:0000305}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01003}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wzyE wzy b3793 JW3769"
---

# wzyE

`protein.P27835`

## Static

- Type: `protein`
- Source: `UniProt:P27835`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01003, ECO:0000305}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01003}.

## Enriched Summary

FUNCTION: Probably involved in the polymerization of enterobacterial common antigen (ECA) trisaccharide repeat units. Required for the assembly of the phosphoglyceride-linked form of ECA (ECA(PG)) and the water-soluble cyclic form of ECA (ECA(CYC)). {ECO:0000269|PubMed:16199561}. The assembly of enterobacterial common antigen (ECA) occurs by a Wzx/Wzy-dependent pathway (see ). wzyE is located immediately downstream of wecF (encoding the 4-alpha-L-fucosyltransferase which catalyses the final step in biosythesis of an ECA trisaccharide) and is suggested to encode a polymerase involved in ECA polysaccharide chain elongation . WzyE is required for the assembly of glycerophosphatidyl-linked ECA (CPD-21605 ECAPG) and cyclic ECA (CPD0-2646 ECACYC) ; WzyE catalyses polymerization of repeat unit Und-P linked saccharides at the periplasmic face of the inner membrane via a 'block-transfer' mechanism with modulation of polysaccharide chain length dependent on EG11295-MONOMER WzzE. The lipid III flippase EG11486-MONOMER WzxE, ECA polymerase WzyE, and co-polymerase EG11295-MONOMER WzzE may function as a multiprotein complex . WzyE and WzzE were shown in TAX-29471 to form a complex in vivo with stoichiometry of approximately eight WzzE to one WzyE . WzyE is highly conserved. Alignment of 248 WzyE sequences from across Enterobacteriales identified 105 residues that are completely conserved...

## Biological Role

Catalyzes RXN-22149 (reaction.ecocyc.RXN-22149), RXN0-7383 (reaction.ecocyc.RXN0-7383).

## Annotation

FUNCTION: Probably involved in the polymerization of enterobacterial common antigen (ECA) trisaccharide repeat units. Required for the assembly of the phosphoglyceride-linked form of ECA (ECA(PG)) and the water-soluble cyclic form of ECA (ECA(CYC)). {ECO:0000269|PubMed:16199561}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-22149|reaction.ecocyc.RXN-22149]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7383|reaction.ecocyc.RXN0-7383]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3793|gene.b3793]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27835`
- `KEGG:ecj:JW3769;eco:b3793;ecoc:C3026_20540;`
- `GeneID:948293;`
- `GO:GO:0005886; GO:0009246; GO:0030247`

## Notes

Probable ECA polymerase
