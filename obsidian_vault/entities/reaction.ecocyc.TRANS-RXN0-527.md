---
entity_id: "reaction.ecocyc.TRANS-RXN0-527"
entity_type: "reaction"
name: "cholate diffusion"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-527"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# cholate diffusion

`reaction.ecocyc.TRANS-RXN0-527`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-527`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

In the acidic pH of the bacterial periplasm, unconjugated bile acids exist largely in an uncharged, protonated form and can diffuse across the cytoplasmic membrane . Their detergent properties are toxic to cells; the TRANS-CPLX-201 "AcrAB-TolC" efflux system and the YJIO-MONOMER "MdtM" efflux antiporter both contribute to E. coli's intrinsic resistance to bile acids . Additionally the presence of a 7-ALPHA-HYDROXYSTEROID-DEH-CPLX in E. coli raises the possibility of detoxification through further metabolism . EcoCyc reaction equation: CHOLATE -> CHOLATE; direction=PHYSIOL-LEFT-TO-RIGHT. In the acidic pH of the bacterial periplasm, unconjugated bile acids exist largely in an uncharged, protonated form and can diffuse across the cytoplasmic membrane . Their detergent properties are toxic to cells; the TRANS-CPLX-201 "AcrAB-TolC" efflux system and the YJIO-MONOMER "MdtM" efflux antiporter both contribute to E. coli's intrinsic resistance to bile acids . Additionally the presence of a 7-ALPHA-HYDROXYSTEROID-DEH-CPLX in E. coli raises the possibility of detoxification through further metabolism .

## Biological Role

Substrates: Cholic acid (molecule.C00695). Products: Cholic acid (molecule.C00695).

## Annotation

In the acidic pH of the bacterial periplasm, unconjugated bile acids exist largely in an uncharged, protonated form and can diffuse across the cytoplasmic membrane . Their detergent properties are toxic to cells; the TRANS-CPLX-201 "AcrAB-TolC" efflux system and the YJIO-MONOMER "MdtM" efflux antiporter both contribute to E. coli's intrinsic resistance to bile acids . Additionally the presence of a 7-ALPHA-HYDROXYSTEROID-DEH-CPLX in E. coli raises the possibility of detoxification through further metabolism .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00695|molecule.C00695]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00695|molecule.C00695]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-527`

## Notes

CHOLATE -> CHOLATE; direction=PHYSIOL-LEFT-TO-RIGHT
