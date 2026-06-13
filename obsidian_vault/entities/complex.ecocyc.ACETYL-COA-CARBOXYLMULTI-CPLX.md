---
entity_id: "complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX"
entity_type: "complex"
name: "acetyl-CoA carboxylase complex"
source_database: "EcoCyc"
source_id: "ACETYL-COA-CARBOXYLMULTI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# acetyl-CoA carboxylase complex

`complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACETYL-COA-CARBOXYLMULTI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX|complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX]], [[complex.ecocyc.BIOTIN-CARBOXYL-CPLX|complex.ecocyc.BIOTIN-CARBOXYL-CPLX]], [[complex.ecocyc.BCCP-CPLX|complex.ecocyc.BCCP-CPLX]]

## Enriched Summary

The acetyl-CoA carboxylase complex is one of the key enzymes in the biosynthesis of fatty acids (see FASYN-INITIAL-PWY). The enzyme belongs to the family of enzymes that catalyze the intermolecular transfer of carboxyl groups via the transient formation of a carboxyphosphate intermediate covalently linked to a biotin prosthetic group . For a thorough discussion of this protein, please see the pathway PWY0-1264. The E. coli enzyme complex is composed of two catalytic units and one carrier protein, encoded by four different genes. The catalytic units are BIOTIN-CARBOXYL-CPLX (BC), an AccC homodimer, and ACETYL-COA-CARBOXYLMULTI-CPLX (ACCT), an AccA2AccD2 heterotetramer. The carrier protein is the BCCP-CPLX (BCCP), an AccB homodimer. The BCCP monomer is biotinylated by the enzyme BIOTINLIG-ENZRXN. Following dimerization of the biotinylated monomers, biotin carboxylase catalyzes the addition of CARBON-DIOXIDE to the carrier protein dimer, forming carboxybiotin-L-lysine-in-BCCP-dimers (carboxy-BCCP). Carboxy-BCCP in turn is the substrate for ACCT, which transfers the carboxy group to ACETYL-COA, resulting in the formation of MALONYL-COA and the regeneration of BCCP. Both biotinylation and carboxylation of the carrier protein require ATP, while the last step, transfer of the carboxy group to acetyl-CoA, does not...

## Annotation

The acetyl-CoA carboxylase complex is one of the key enzymes in the biosynthesis of fatty acids (see FASYN-INITIAL-PWY). The enzyme belongs to the family of enzymes that catalyze the intermolecular transfer of carboxyl groups via the transient formation of a carboxyphosphate intermediate covalently linked to a biotin prosthetic group . For a thorough discussion of this protein, please see the pathway PWY0-1264. The E. coli enzyme complex is composed of two catalytic units and one carrier protein, encoded by four different genes. The catalytic units are BIOTIN-CARBOXYL-CPLX (BC), an AccC homodimer, and ACETYL-COA-CARBOXYLMULTI-CPLX (ACCT), an AccA2AccD2 heterotetramer. The carrier protein is the BCCP-CPLX (BCCP), an AccB homodimer. The BCCP monomer is biotinylated by the enzyme BIOTINLIG-ENZRXN. Following dimerization of the biotinylated monomers, biotin carboxylase catalyzes the addition of CARBON-DIOXIDE to the carrier protein dimer, forming carboxybiotin-L-lysine-in-BCCP-dimers (carboxy-BCCP). Carboxy-BCCP in turn is the substrate for ACCT, which transfers the carboxy group to ACETYL-COA, resulting in the formation of MALONYL-COA and the regeneration of BCCP. Both biotinylation and carboxylation of the carrier protein require ATP, while the last step, transfer of the carboxy group to acetyl-CoA, does not . Coordinated overexpression of accA, accB, accC and accD increases the biosynthesis of fatty acids . Review:

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_component_of` <-- [[complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX|complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.BCCP-CPLX|complex.ecocyc.BCCP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.BIOTIN-CARBOXYL-CPLX|complex.ecocyc.BIOTIN-CARBOXYL-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A9Q5|protein.P0A9Q5]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0ABD5|protein.P0ABD5]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P24182|protein.P24182]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ACETYL-COA-CARBOXYLMULTI-CPLX`
- `PDB:2F9Y`
- `QSPROTEOME:QS00196499`

## Notes

1*complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX|1*complex.ecocyc.BIOTIN-CARBOXYL-CPLX|1*complex.ecocyc.BCCP-CPLX
