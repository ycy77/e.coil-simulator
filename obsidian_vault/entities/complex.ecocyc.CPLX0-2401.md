---
entity_id: "complex.ecocyc.CPLX0-2401"
entity_type: "complex"
name: "tryptophan synthase, β subunit dimer"
source_database: "EcoCyc"
source_id: "CPLX0-2401"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "TSase &beta"
  - "2"
  - "B protein"
  - "&beta"
  - "<sub>2</sub> protein"
---

# tryptophan synthase, β subunit dimer

`complex.ecocyc.CPLX0-2401`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2401`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A879|protein.P0A879]]

## Enriched Summary

The TrpB polypeptide functions as the β subunit of the tetrameric (α2-β2) tryptophan synthase complex . The TrpB protein forms a homodimer (TSase β2) in which each subunit contains a molecule of the cofactor pyridoxal 5'-phosphate (PLP) covalently linked to the ε-amino group of a lysine residue via a Schiff base . This complex catalyzes the synthesis of L-tryptophan from indole and L-serine, also termed the β reaction. The β2 subunit possesses binding sites for L-serine and PLP and can catalyze a variety of reactions involving these compounds . The apo-β2 subunit has been used as a model system to study the mechanism of folding of protein oligomers . The crystal structure of the holo-tryptophan synthase β-subunit from Escherichia coli has been determined . Review: . The TrpB polypeptide functions as the β subunit of the tetrameric (α2-β2) tryptophan synthase complex . The TrpB protein forms a homodimer (TSase β2) in which each subunit contains a molecule of the cofactor pyridoxal 5'-phosphate (PLP) covalently linked to the ε-amino group of a lysine residue via a Schiff base . This complex catalyzes the synthesis of L-tryptophan from indole and L-serine, also termed the β reaction. The β2 subunit possesses binding sites for L-serine and PLP and can catalyze a variety of reactions involving these compounds...

## Biological Role

Catalyzes RXN0-2382 (reaction.ecocyc.RXN0-2382). Component of tryptophan synthase (complex.ecocyc.TRYPSYN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

The TrpB polypeptide functions as the β subunit of the tetrameric (α2-β2) tryptophan synthase complex . The TrpB protein forms a homodimer (TSase β2) in which each subunit contains a molecule of the cofactor pyridoxal 5'-phosphate (PLP) covalently linked to the ε-amino group of a lysine residue via a Schiff base . This complex catalyzes the synthesis of L-tryptophan from indole and L-serine, also termed the β reaction. The β2 subunit possesses binding sites for L-serine and PLP and can catalyze a variety of reactions involving these compounds . The apo-β2 subunit has been used as a model system to study the mechanism of folding of protein oligomers . The crystal structure of the holo-tryptophan synthase β-subunit from Escherichia coli has been determined . Review: .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2382|reaction.ecocyc.RXN0-2382]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.TRYPSYN|complex.ecocyc.TRYPSYN]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A879|protein.P0A879]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-2401`
- `QSPROTEOME:QS00188553`

## Notes

2*protein.P0A879
