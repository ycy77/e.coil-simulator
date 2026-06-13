---
entity_id: "reaction.ecocyc.RXN0-3241"
entity_type: "reaction"
name: "RXN0-3241"
source_database: "EcoCyc"
source_id: "RXN0-3241"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3241

`reaction.ecocyc.RXN0-3241`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3241`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the hydrolysis of a β peptide bond formed between the side-chain carboxyl group of an aspartate residue and some other amino acid. This reaction has maximum activity for cleavage of an aspartyl-leucine dipeptide. Relative activity for hydrolysis of other dipeptides is lower: aspartyl-serine (82%), aspartyl-methionine (68%), aspartyl-valine (56%), aspartyl-glutamate (48%), aspartyl-phenylalanine (38%), aspartyl-alanine (33%), aspartyl-isoleucine (19%), aspartyl-threonine (18%). This reaction has no activity for cleavage of aspartyl-glycine, aspartyl-histidine, or tripeptides. EcoCyc reaction equation: CPD-12991 + WATER -> L-ASPARTATE + Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolysis of a β peptide bond formed between the side-chain carboxyl group of an aspartate residue and some other amino acid. This reaction has maximum activity for cleavage of an aspartyl-leucine dipeptide. Relative activity for hydrolysis of other dipeptides is lower: aspartyl-serine (82%), aspartyl-methionine (68%), aspartyl-valine (56%), aspartyl-glutamate (48%), aspartyl-phenylalanine (38%), aspartyl-alanine (33%), aspartyl-isoleucine (19%), aspartyl-threonine (18%). This reaction has no activity for cleavage of aspartyl-glycine, aspartyl-histidine, or tripeptides.

## Biological Role

Catalyzed by isoaspartyl dipeptidase / asparaginase 3 (complex.ecocyc.CPLX0-263), isoaspartyl dipeptidase (complex.ecocyc.CPLX0-3021). Substrates: H2O (molecule.C00001), β-aspartyl dipeptide (molecule.ecocyc.CPD-12991). Products: L-Aspartate (molecule.C00049), a proteinogenic amino acid (molecule.ecocyc.Amino-Acids-20).

## Annotation

This reaction is the hydrolysis of a β peptide bond formed between the side-chain carboxyl group of an aspartate residue and some other amino acid. This reaction has maximum activity for cleavage of an aspartyl-leucine dipeptide. Relative activity for hydrolysis of other dipeptides is lower: aspartyl-serine (82%), aspartyl-methionine (68%), aspartyl-valine (56%), aspartyl-glutamate (48%), aspartyl-phenylalanine (38%), aspartyl-alanine (33%), aspartyl-isoleucine (19%), aspartyl-threonine (18%). This reaction has no activity for cleavage of aspartyl-glycine, aspartyl-histidine, or tripeptides.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-263|complex.ecocyc.CPLX0-263]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3021|complex.ecocyc.CPLX0-3021]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids-20|molecule.ecocyc.Amino-Acids-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12991|molecule.ecocyc.CPD-12991]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3241`

## Notes

CPD-12991 + WATER -> L-ASPARTATE + Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT
