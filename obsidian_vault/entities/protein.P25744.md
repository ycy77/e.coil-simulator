---
entity_id: "protein.P25744"
entity_type: "protein"
name: "mdtG"
source_database: "UniProt"
source_id: "P25744"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtG yceE b1053 JW1040"
---

# mdtG

`protein.P25744`

## Static

- Type: `protein`
- Source: `UniProt:P25744`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Confers resistance to fosfomycin and deoxycholate. {ECO:0000269|PubMed:11566977}. Increased expression of mdtG in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) results in a four-fold increase in resistance to fosfomycin and a two-fold increase in resistance to deoxycholate but does not impact the resistance to a range of other antibiotics and toxic compounds . MdtG (formerly YceE) is a member of the Drug:H+ Antiporter-1 (12 Spanner) (DHA1) family within the Major Facilitator Superfamily (MFS) . mdtG is a member of the marA-soxS-rob regulon; a SoxS binding marbox sequence is located within the mdtG promoter region; an mdtG-lacZ transcriptional fusion is induced in the presence of paraquat, sodium salicylate and 2,2'-dipyridyl . mdtG is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Biological Role

Catalyzes fosfomycin:proton antiport (reaction.ecocyc.TRANS-RXN-342), deoxycholate:proton antiport (reaction.ecocyc.TRANS-RXN0-589). Transports Deoxycholic acid (molecule.C04483), fosfomycin (molecule.ecocyc.CPD0-1113), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Confers resistance to fosfomycin and deoxycholate. {ECO:0000269|PubMed:11566977}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-342|reaction.ecocyc.TRANS-RXN-342]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-589|reaction.ecocyc.TRANS-RXN0-589]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD0-1113|molecule.ecocyc.CPD0-1113]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1053|gene.b1053]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25744`
- `KEGG:ecj:JW1040;eco:b1053;ecoc:C3026_06410;`
- `GeneID:75203640;945627;`
- `GO:GO:0005886; GO:0022857; GO:0046677; GO:1901562; GO:1990961`

## Notes

Multidrug resistance protein MdtG
