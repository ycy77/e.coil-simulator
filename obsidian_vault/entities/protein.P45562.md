---
entity_id: "protein.P45562"
entity_type: "protein"
name: "xapB"
source_database: "UniProt"
source_id: "P45562"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11466294, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:7559336}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xapB b2406 JW2397"
---

# xapB

`protein.P45562`

## Static

- Type: `protein`
- Source: `UniProt:P45562`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11466294, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:7559336}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Uptake of xanthosine (PubMed:11466294). Can also transport other nucleosides such as inosine, adenosine, cytidine, uridine and thymidine (PubMed:11466294). Transport is driven by a proton motive force (PubMed:11466294). {ECO:0000269|PubMed:11466294}. XapB is a probable xanthosine transporter. The xapB gene is located in a xanthosine-inducible operon with xapA, encoding xanthosine phosphorylase . Growth on xanthosine is greatly reduced in xapB mutants, and XapB was demonstrated to fractionate with the cell membrane. XapB is a member of the major facilitator superfamily of transporters and shares a high degree of similarity with the nucleoside transporter NupG . XapB therefore is probably a xanthosine/proton symporter. Imported xanthosine is cleaved by XapA to yield xanthine which can be used in nucleotide synthesis or as a nitrogen source, and ribose-1-phosphate which can be used as a carbon source.

## Biological Role

Catalyzes xanthosine:proton symport (reaction.ecocyc.TRANS-RXN-31). Transports Xanthosine (molecule.C01762), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Uptake of xanthosine (PubMed:11466294). Can also transport other nucleosides such as inosine, adenosine, cytidine, uridine and thymidine (PubMed:11466294). Transport is driven by a proton motive force (PubMed:11466294). {ECO:0000269|PubMed:11466294}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-31|reaction.ecocyc.TRANS-RXN-31]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C01762|molecule.C01762]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2406|gene.b2406]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45562`
- `KEGG:ecj:JW2397;eco:b2406;ecoc:C3026_13375;`
- `GeneID:946868;`
- `GO:GO:0005337; GO:0005886; GO:0015212; GO:0015213; GO:0015293; GO:0015553; GO:0015858; GO:0016020; GO:0055086`

## Notes

Xanthosine permease (Xanthosine transporter)
