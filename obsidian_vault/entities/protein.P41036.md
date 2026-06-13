---
entity_id: "protein.P41036"
entity_type: "protein"
name: "nanT"
source_database: "UniProt"
source_id: "P41036"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01238, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01238}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nanT b3224 JW3193"
---

# nanT

`protein.P41036`

## Static

- Type: `protein`
- Source: `UniProt:P41036`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01238, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01238}.

## Enriched Summary

FUNCTION: Catalyzes the proton-dependent transport of sialic acid (PubMed:22167185, PubMed:23848303). Can transport the common sialic acid N-acetylneuraminic acid (Neu5Ac) and the related sialic acids N-glycolylneuraminic acid (Neu5Gc) and 3-keto-3-deoxy-D-glycero-D-galactonononic acid (KDN) (PubMed:23848303). Functions as a bidirectional transporter in vitro (PubMed:22167185). {ECO:0000269|PubMed:22167185, ECO:0000269|PubMed:23848303}. E. coli K-12 is able to use the common sialic acid, N-acetylneuramic acid, as a carbon source and possesses a transporter, NanT, with high specificity for this sugar acid . NanT recognizes the abundant β-anomer of N-acetylneuramic acid; expression of a periplasmic CPLX0-7658 supports the ability to use the less abundant α-anomer in vivo . Purified NanT, reconstituted into liposomes, mediates the uptake of labeled N-acetylneuraminate in vitro and transport is energised by the proton gradient alone . NanT facilitates both substrate counterflow and substrate exchange in vitro (see also ). NanT transports the related sialic acids, CPD-273 and CPD-21259 "3-deoxy-D-glycero-D-galactonononate" (KDN) and the anhydro-sialic acid CPD-23638 . NanT transports exogenous 3-deoxy-D-manno-oct-2-ulosonic acid (Kdo) and its experimentally useful azido analog, 8-azido-3,8-dideoxy-D-manno-oct-2-ulosonic acid (Kdo-N3)...

## Biological Role

Catalyzes N-acetylneuraminate:proton symport (reaction.ecocyc.RXN-15314). Transports hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Catalyzes the proton-dependent transport of sialic acid (PubMed:22167185, PubMed:23848303). Can transport the common sialic acid N-acetylneuraminic acid (Neu5Ac) and the related sialic acids N-glycolylneuraminic acid (Neu5Gc) and 3-keto-3-deoxy-D-glycero-D-galactonononic acid (KDN) (PubMed:23848303). Functions as a bidirectional transporter in vitro (PubMed:22167185). {ECO:0000269|PubMed:22167185, ECO:0000269|PubMed:23848303}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-15314|reaction.ecocyc.RXN-15314]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3224|gene.b3224]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P41036`
- `KEGG:ecj:JW3193;eco:b3224;ecoc:C3026_17540;`
- `GeneID:947740;`
- `GO:GO:0005886; GO:0015538; GO:0015739; GO:0046942; GO:0046943`

## Notes

Sialic acid transporter NanT (Sialic acid permease) (Sialic acid/H(+) symporter)
