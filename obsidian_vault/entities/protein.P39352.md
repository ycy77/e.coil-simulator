---
entity_id: "protein.P39352"
entity_type: "protein"
name: "nanX"
source_database: "UniProt"
source_id: "P39352"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:32542330}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nanX yjhB b4279 JW5768"
---

# nanX

`protein.P39352`

## Static

- Type: `protein`
- Source: `UniProt:P39352`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:32542330}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Probably transports across the inner membrane the two dehydrated forms of N-acetylneuraminate (Neu5Ac), 2,7-anhydro-N-acetylneuraminate (2,7-AN) and 2-deoxy-2,3-didehydro-N-acetylneuraminate (2,3-EN). {ECO:0000269|PubMed:32542330, ECO:0000269|PubMed:32669363}. nanX encodes an inner membrane transporter that appears specific for CPD-6182 (2,7-AN) - a dehydrated form of the abundant sialic acid N-ACETYLNEURAMINATE "N-acetylneuraminate". In an engineered strain lacking sialic acid transporters and expressing the sialic acid utilisation pathway constitutively (E. coli BW25113 ΔnanT::FRT ΔnanX::F3 ΔnanR ΔnagC), the expression of recombinant NanX supports growth with 2,7-anhydro-N-acetylneuraminate as sole carbon source but does not support growth with CPD-23638 (2,3-EN) nor with N-acetylneuraminate . Deletion of nanX (in strain BW25113) results in complete loss of in vitro growth on 2,7-AN; NanX, functioning together with a co-expressed CPLX0-8544 hydratase, likely supports scavenging of 2,7-AN in the human gut (see also ). NanX is a member of the Major Facilitator Superfamily of transporters and it has sequence homology (35% identity, 55% similarity) with the NANT-MONOMER "N-acetylneuraminate:H+ symporter" NanT . NanX is an archetypal member of the bacterial sialic acid transporter 1 (ST1) family...

## Biological Role

Catalyzes 2,7-anhydro-N-acetylneuraminate:H+ symport (reaction.ecocyc.TRANS-RXN-415). Transports hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Probably transports across the inner membrane the two dehydrated forms of N-acetylneuraminate (Neu5Ac), 2,7-anhydro-N-acetylneuraminate (2,7-AN) and 2-deoxy-2,3-didehydro-N-acetylneuraminate (2,3-EN). {ECO:0000269|PubMed:32542330, ECO:0000269|PubMed:32669363}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-415|reaction.ecocyc.TRANS-RXN-415]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4279|gene.b4279]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39352`
- `KEGG:ecj:JW5768;eco:b4279;ecoc:C3026_23075;`
- `GeneID:948807;`
- `GO:GO:0005886; GO:0046942; GO:0046943`

## Notes

Sialic acid transporter NanX
