---
entity_id: "complex.ecocyc.URACIL-PRIBOSYLTRANS-CPLX"
entity_type: "complex"
name: "uracil phosphoribosyltransferase"
source_database: "EcoCyc"
source_id: "URACIL-PRIBOSYLTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# uracil phosphoribosyltransferase

`complex.ecocyc.URACIL-PRIBOSYLTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:URACIL-PRIBOSYLTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A8F0|protein.P0A8F0]]

## Enriched Summary

Uracil phosphoribosyltransferase (UPRT) is a pyrimidine salvage enzyme that catalyzes the synthesis of uridine 5'-monophosphate (UMP) from uracil and 5-phospho-α-D-ribose 1-diphosphate (PRPP). UMP is the precursor of all pyrimidine ribonucleotides as shown in pathway PWY-7176. Pyrimidine salvage enables E. coli to utilize preformed nucleobases and nucleosides either from the degradation products of cellular nucleic acids, or from the growth medium . The enzyme has been purified from cell extracts and shown to be a homotrimer. It is specific for uracil as substrate and can utilize some uracil analogs . Subsequent work showed that upon exposure to substrate PRPP and allosteric effector GTP, the E. coli K-12 enzyme undergoes a slow, concentration-dependent activation that involves transformation of the trimeric form to a more active pentameric or hexameric form. A Mg2+-PRPP complex, rather than free PRPP, was shown to be the true substrate. In addition to GTP, the regulatory nucleotide ppGpp can also activate the enzyme . Like other uracil phosphoribosyltransferases the E. coli enzyme contains a catalytically important conserved proline residue in its PRPP binding site. The enzyme utilizes a sequential mechanism in which PRPP binds prior to uracil . The crystal structure of uracil phosphoribosyltransferase was solved at 2...

## Biological Role

Catalyzes URACIL-PRIBOSYLTRANS-RXN (reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Uracil phosphoribosyltransferase (UPRT) is a pyrimidine salvage enzyme that catalyzes the synthesis of uridine 5'-monophosphate (UMP) from uracil and 5-phospho-α-D-ribose 1-diphosphate (PRPP). UMP is the precursor of all pyrimidine ribonucleotides as shown in pathway PWY-7176. Pyrimidine salvage enables E. coli to utilize preformed nucleobases and nucleosides either from the degradation products of cellular nucleic acids, or from the growth medium . The enzyme has been purified from cell extracts and shown to be a homotrimer. It is specific for uracil as substrate and can utilize some uracil analogs . Subsequent work showed that upon exposure to substrate PRPP and allosteric effector GTP, the E. coli K-12 enzyme undergoes a slow, concentration-dependent activation that involves transformation of the trimeric form to a more active pentameric or hexameric form. A Mg2+-PRPP complex, rather than free PRPP, was shown to be the true substrate. In addition to GTP, the regulatory nucleotide ppGpp can also activate the enzyme . Like other uracil phosphoribosyltransferases the E. coli enzyme contains a catalytically important conserved proline residue in its PRPP binding site. The enzyme utilizes a sequential mechanism in which PRPP binds prior to uracil . The crystal structure of uracil phosphoribosyltransferase was solved at 2.8 Å resolution (see the PDB link below), but no accompanying paper has been published. A subsequent in silico analysis of this structural data described four chains that form two tight dimers in the crystal . Deletion of upp prevents the uptake of uracil by CPLX0-8247 UraA and by B1006-MONOMER RutG; UPRT activity is rate-limiting for transport by UraA; UPRT activity sustains UraA-mediated uptake of uracil by facilitated diffusion . Purified UPRT displays

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN|reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A8F0|protein.P0A8F0]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:URACIL-PRIBOSYLTRANS-CPLX`
- `QSPROTEOME:QS00049562`

## Notes

3*protein.P0A8F0
