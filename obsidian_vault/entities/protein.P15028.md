---
entity_id: "protein.P15028"
entity_type: "protein"
name: "fecB"
source_database: "UniProt"
source_id: "P15028"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2651410, ECO:0000269|PubMed:2836368}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fecB b4290 JW4250"
---

# fecB

`protein.P15028`

## Static

- Type: `protein`
- Source: `UniProt:P15028`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2651410, ECO:0000269|PubMed:2836368}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex FecBCDE involved in citrate-dependent Fe(3+) uptake (PubMed:17660286, PubMed:2651410). Binds both iron-free and iron-loaded citrate although it binds iron-loaded citrate with a higher affinity (PubMed:26600288). Binds different forms of Fe(3+)-citrate as well as citrate complexed with various representative Fe(3+)-mimics (Ga(3+), Al(3+), Sc(3+) and In(3+)) and a representative divalent metal ion (Mg(2+)) (PubMed:26600288). Can also bind various tricarboxylates in iron-free and iron-loaded form (PubMed:26600288). {ECO:0000269|PubMed:17660286, ECO:0000269|PubMed:2651410, ECO:0000269|PubMed:26600288}. fecB encodes the periplasmic substrate binding component of the iron dicitrate ABC transporter. FecB is a Class III periplasmic binding protein - it is predicted to be a bilobal protein with a single α-helical hinge connecting the two lobes . Purified FecB binds both iron-free and iron-loaded citrate at pH 5.5 and pH 8; purified FecB binds [Fe2(cit)2]2- (di-iron dicitrate) and [Fe(cit)2]5- (iron dicitrate) with similar affinity; purified FecB binds the tricarboxylates isocitrate and cis-aconitic acid and the citric acid derivatives tricarballyic acid and hydroxycitrate; purified FecB binds with other metal-citrate complexes, including Ga3+-citrate, Al3+-citrate and In3+-citrate .

## Biological Role

Component of ferric citrate ABC transporter (complex.ecocyc.ABC-9-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex FecBCDE involved in citrate-dependent Fe(3+) uptake (PubMed:17660286, PubMed:2651410). Binds both iron-free and iron-loaded citrate although it binds iron-loaded citrate with a higher affinity (PubMed:26600288). Binds different forms of Fe(3+)-citrate as well as citrate complexed with various representative Fe(3+)-mimics (Ga(3+), Al(3+), Sc(3+) and In(3+)) and a representative divalent metal ion (Mg(2+)) (PubMed:26600288). Can also bind various tricarboxylates in iron-free and iron-loaded form (PubMed:26600288). {ECO:0000269|PubMed:17660286, ECO:0000269|PubMed:2651410, ECO:0000269|PubMed:26600288}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-9-CPLX|complex.ecocyc.ABC-9-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4290|gene.b4290]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15028`
- `KEGG:ecj:JW4250;eco:b4290;ecoc:C3026_23135;`
- `GeneID:946838;`
- `GO:GO:0006879; GO:0010039; GO:0016020; GO:0030288; GO:0033212; GO:0033214; GO:0055052`

## Notes

Fe(3+) dicitrate-binding periplasmic protein FecB (Iron(III) dicitrate-binding periplasmic protein)
