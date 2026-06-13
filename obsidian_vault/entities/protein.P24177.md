---
entity_id: "protein.P24177"
entity_type: "protein"
name: "acrD"
source_database: "UniProt"
source_id: "P24177"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acrD yffA b2470 JW2454"
---

# acrD

`protein.P24177`

## Static

- Type: `protein`
- Source: `UniProt:P24177`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Participates in the efflux of aminoglycosides. Confers resistance to a variety of these substances. {ECO:0000269|PubMed:10692383}. AcrD is a member of the resistance-nodulation-division (RND) superfamily and a component of the AcrAD-TolC efflux pump complex in E. coli K-12. AcrD is homologous to the major efflux pump permease AcrB . Disruption of acrD in the K-12 strain JC7623 increases susceptibility to a range of aminoglycoside antibiotics (amikacin, gentamicin, tobramycin, kanamycin and neomycin) and cells accumulate higher levels of labeled dihydrostreptomycin and gentamicin than the parent strain; disruption of acrD in the K-12 strain JC7623 slightly increases susceptibility to erythromycin and puromycin but does not affect susceptibility to a range of other compounds including crystal violet, novobiocin, rifampin, chloramphenicol, carbenicillin, cefoxitin, nalidixic acid, norfloxacin and ampicillin (see also ). Expression of cloned acrD in the K-12 strain KAM3 which lacks AcrB (see ) confers increased resistance to deoxycholate, SDS, novobiocin and kanamycin (compared to the mutant parent); overexpression of acrD in the KAM3 strain confers a slightly increased resistance to tetracycline, nalidixic acid, norfloxacin and fosfomycin (compared to the mutant parent) (see also )...

## Biological Role

Component of multidrug efflux pump AcrAD-TolC (complex.ecocyc.CPLX0-3932).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Participates in the efflux of aminoglycosides. Confers resistance to a variety of these substances. {ECO:0000269|PubMed:10692383}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3932|complex.ecocyc.CPLX0-3932]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b2470|gene.b2470]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24177`
- `KEGG:ecj:JW2454;eco:b2470;ecoc:C3026_13700;`
- `GeneID:945464;`
- `GO:GO:0005886; GO:0009636; GO:0015125; GO:0015562; GO:0015721; GO:0016020; GO:0042908; GO:0042910; GO:0046677; GO:0098567; GO:0140330; GO:1990281`

## Notes

Probable aminoglycoside efflux pump (Acriflavine resistance protein D)
