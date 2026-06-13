---
entity_id: "protein.P0AC69"
entity_type: "protein"
name: "grxD"
source_database: "UniProt"
source_id: "P0AC69"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:15833738}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "grxD ydhD b1654 JW1646"
---

# grxD

`protein.P0AC69`

## Static

- Type: `protein`
- Source: `UniProt:P0AC69`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:15833738}.

## Enriched Summary

FUNCTION: Monothiol glutaredoxin involved in the biogenesis of iron-sulfur clusters. {ECO:0000305}. GrxD belongs to the family of monothiol glutaredoxins. The dimeric GrxD can act as a scaffold protein, transferring an intact [2Fe-2S] cluster to the model acceptor protein ferredoxin . Oxidized GrxD can be reduced by the glutaredoxin (RED-GLUTAREDOXIN) or thioredoxin (THIOREDOXIN-REDUCT-NADPH-MONOMER) system. GrxD is not active in the standard glutaredoxin (GLUTATHIONE-SYN-CPLX) assay . A solution structure of the reduced form of GrxD has been determined . A crystal structure of the GrxD dimer coordinating a [2Fe-2S] cluster at the dimer interface has been solved. This arrangement suggests that GrxD has to undergo a conformational change to release the [2Fe-2S] cluster . Physical and genetic interactions with iron-sulfur cluster assembly proteins suggest that GrxD acts as a scaffold and/or transfer protein for iron-sulfur clusters to the CPLX0-246 "cysteine desulfurase" (SUF) and CPLX0-7838 (CSD) sulfur transfer systems. Both GrxD and CPLX0-7682 "NfuA" interact with G6364-MONOMER "MiaB". NfuA, but not GrxD, can transfer a 4Fe-4S cluster to apo-MiaB in vitro, and both proteins affect MiaB activity in vivo . GrxD is an abundant protein that is upregulated upon iron depletion and during stationary phase; the increased expression is dependent on ppGpp...

## Biological Role

Component of glutaredoxin 4 (complex.ecocyc.CPLX0-7817), Grx4-BolA complex (complex.ecocyc.CPLX0-7942), Grx4-IbaG complex (complex.ecocyc.CPLX0-8239).

## Annotation

FUNCTION: Monothiol glutaredoxin involved in the biogenesis of iron-sulfur clusters. {ECO:0000305}.

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7817|complex.ecocyc.CPLX0-7817]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7942|complex.ecocyc.CPLX0-7942]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8239|complex.ecocyc.CPLX0-8239]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1654|gene.b1654]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC69`
- `KEGG:ecj:JW1646;eco:b1654;ecoc:C3026_09490;`
- `GeneID:86859582;89516419;946169;`
- `GO:GO:0005829; GO:0006879; GO:0015036; GO:0016226; GO:0042803; GO:0045454; GO:0046872; GO:0051537; GO:1990229`

## Notes

Glutaredoxin 4 (Grx4) (Monothiol glutaredoxin)
