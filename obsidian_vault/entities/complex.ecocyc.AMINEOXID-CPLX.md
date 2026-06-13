---
entity_id: "complex.ecocyc.AMINEOXID-CPLX"
entity_type: "complex"
name: "copper-containing amine oxidase"
source_database: "EcoCyc"
source_id: "AMINEOXID-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# copper-containing amine oxidase

`complex.ecocyc.AMINEOXID-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:AMINEOXID-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PERI-BAC-GN
- Complex type: `structural`
- Components: [[protein.P46883|protein.P46883]]

## Enriched Summary

E. coli K-12 is capable of growth on phenylethylamine as the sole carbon and energy source. Phenylethylamine oxidase catalyzes the first step in the degradation pathway. This is a particular instance of a reaction catalyzed by the amine oxidase enzyme . In another instance, amine oxidase could hypothetically convert aminoacetone to methylglyoxal, similar to the eukaryotic semicarbazide-sensitive, Cu2+-dependent amine oxidases. This is predicted and discussed in pathway THRDLCTCAT-PWY. Amine oxidase catalyzes the conversion of an aliphatic amine to an aldehyde, followed by a two-electron reduction of O2 to H2O2 to regenerate the oxidized enzyme . It has been proven that the oxidase coded for by the maoA gene uses copper and topaquinone as prosthetic groups. The topaquinone is a part of the polypeptide chain and is generated through the post-translational modification of a protein tyrosine residue, that occurs as a copper-dependent, probably autocatalytic reaction . The enzyme has been crystallized and its reaction mechanism studied by structural analysis . Structural studies using xenon as a probe have suggested that oxygen is likely to access the enzyme active site via a conserved β sandwich . In addition to copper at the catalytic center, there are two peripheral calcium ions bound per monomer...

## Biological Role

Catalyzes AMACETOXID-RXN (reaction.ecocyc.AMACETOXID-RXN), Aliphatic-amine oxidase (reaction.ecocyc.AMINEOXID-RXN), phenylethylamine oxidase (reaction.ecocyc.RXN-10817), RXN-9597 (reaction.ecocyc.RXN-9597). Bound by Cu2+ (molecule.ecocyc.CU_2), topaquinone (molecule.ecocyc.TOPAQUINONE).

## Annotation

E. coli K-12 is capable of growth on phenylethylamine as the sole carbon and energy source. Phenylethylamine oxidase catalyzes the first step in the degradation pathway. This is a particular instance of a reaction catalyzed by the amine oxidase enzyme . In another instance, amine oxidase could hypothetically convert aminoacetone to methylglyoxal, similar to the eukaryotic semicarbazide-sensitive, Cu2+-dependent amine oxidases. This is predicted and discussed in pathway THRDLCTCAT-PWY. Amine oxidase catalyzes the conversion of an aliphatic amine to an aldehyde, followed by a two-electron reduction of O2 to H2O2 to regenerate the oxidized enzyme . It has been proven that the oxidase coded for by the maoA gene uses copper and topaquinone as prosthetic groups. The topaquinone is a part of the polypeptide chain and is generated through the post-translational modification of a protein tyrosine residue, that occurs as a copper-dependent, probably autocatalytic reaction . The enzyme has been crystallized and its reaction mechanism studied by structural analysis . Structural studies using xenon as a probe have suggested that oxygen is likely to access the enzyme active site via a conserved β sandwich . In addition to copper at the catalytic center, there are two peripheral calcium ions bound per monomer . Binding of metal ions at these peripheral sites is important for maximal enzyme activity . The roles of catalytically important residues such as Asp-383 and Tyr-381 have been studied by kinetic analysis using mutant enzymes . Under anaerobiosis, FNR activates tynA gene expression, but it is not known if this regulation is direct or indirect .

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.AMACETOXID-RXN|reaction.ecocyc.AMACETOXID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.AMINEOXID-RXN|reaction.ecocyc.AMINEOXID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10817|reaction.ecocyc.RXN-10817]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9597|reaction.ecocyc.RXN-9597]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.TOPAQUINONE|molecule.ecocyc.TOPAQUINONE]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P46883|protein.P46883]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:AMINEOXID-CPLX`
- `QSPROTEOME:QS00183253`

## Notes

2*protein.P46883
