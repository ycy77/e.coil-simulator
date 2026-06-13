---
entity_id: "complex.ecocyc.TRYPSYN"
entity_type: "complex"
name: "tryptophan synthase"
source_database: "EcoCyc"
source_id: "TRYPSYN"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tryptophan synthase

`complex.ecocyc.TRYPSYN`

## Static

- Type: `complex`
- Source: `EcoCyc:TRYPSYN`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A877|protein.P0A877]], [[complex.ecocyc.CPLX0-2401|complex.ecocyc.CPLX0-2401]]

## Enriched Summary

The physiologically active form of tryptophan synthase is a tetrameric α2-β2 complex consisting of two α subunits (the protein product of the trpA gene) and a dimer of two β subunits (the protein product of the trpB gene). This complex catalyzes the last two steps in the biosynthesis of tryptophan . Although the α2-β2 complex from Escherichia coli has been well studied, the purified α2-β2 complex from Salmonella enterica subsp. enterica serovar Typhimurium (Salmonella typhimurium) provided crystals suitable for X-ray crystallography. Thus, the complex from this species has been studied in greater detail (reviewed in ). The physiologically active form of tryptophan synthase is a tetrameric α2-β2 complex consisting of two α subunits (the protein product of the trpA gene) and a dimer of two β subunits (the protein product of the trpB gene). This complex catalyzes the last two steps in the biosynthesis of tryptophan . Although the α2-β2 complex from Escherichia coli has been well studied, the purified α2-β2 complex from Salmonella enterica subsp. enterica serovar Typhimurium (Salmonella typhimurium) provided crystals suitable for X-ray crystallography. Thus, the complex from this species has been studied in greater detail (reviewed in ).

## Biological Role

Catalyzes TRYPSYN-RXN (reaction.ecocyc.TRYPSYN-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

The physiologically active form of tryptophan synthase is a tetrameric α2-β2 complex consisting of two α subunits (the protein product of the trpA gene) and a dimer of two β subunits (the protein product of the trpB gene). This complex catalyzes the last two steps in the biosynthesis of tryptophan . Although the α2-β2 complex from Escherichia coli has been well studied, the purified α2-β2 complex from Salmonella enterica subsp. enterica serovar Typhimurium (Salmonella typhimurium) provided crystals suitable for X-ray crystallography. Thus, the complex from this species has been studied in greater detail (reviewed in ).

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRYPSYN-RXN|reaction.ecocyc.TRYPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.CPLX0-2401|complex.ecocyc.CPLX0-2401]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A877|protein.P0A877]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A879|protein.P0A879]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TRYPSYN`
- `QSPROTEOME:QS00191567`

## Notes

2*protein.P0A877|1*complex.ecocyc.CPLX0-2401
