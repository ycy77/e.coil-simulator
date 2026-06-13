---
entity_id: "protein.P69856"
entity_type: "protein"
name: "nanC"
source_database: "UniProt"
source_id: "P69856"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:19796645}; Multi-pass membrane protein {ECO:0000269|PubMed:19796645}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nanC yjhA b4311 JW5778"
---

# nanC

`protein.P69856`

## Static

- Type: `protein`
- Source: `UniProt:P69856`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:19796645}; Multi-pass membrane protein {ECO:0000269|PubMed:19796645}.

## Enriched Summary

FUNCTION: Outer membrane channel protein allowing the entry of N-acetylneuraminic acid (Neu5Ac, the most abundant sialic acid on host cell surfaces) into the bacteria (PubMed:15743943, PubMed:22246445). NanC proteins form high-conductance channels which are open at low membrane potentials and which have a weak anion selectivity (PubMed:15743943). {ECO:0000269|PubMed:15743943, ECO:0000269|PubMed:22246445}. nanC encodes an N-acetylneuraminic acid-inducible outer membrane channel; purified NanC reconstituted into liposomes functions as a voltage-dependent, high-conductance channel with weak anion selectivity (see further ); NanC is necessary for growth on N-acetylneuraminic acid (NeuNAc) as a carbon source when the general porins OmpF and OmpC are absent . In the crystal structure reported by NanC forms a barrel composed of 12-antiparallel β-strands with a transmembrane channel whose properties are well suited for the translocation of acidic oligosaccharides. nanC forms a putative operon with nanM and nanS. Expression of nanC is induced by NeuNAc and is modulated by N-acetylglucosamine . nanC is a member of the G7678-MONOMER NanR 'sialoregulon' In the Transporter Classification Database NanC is a member of the Oligogalacturonate-specific Porin (KdgM) family within the Outer Membrane Pore-forming Protein I (OMPP-I) superfamily. nan: N-acylneuraminate: Related reviews:

## Biological Role

Catalyzes RXN-15315 (reaction.ecocyc.RXN-15315), RXN0-0 (reaction.ecocyc.RXN0-0).

## Annotation

FUNCTION: Outer membrane channel protein allowing the entry of N-acetylneuraminic acid (Neu5Ac, the most abundant sialic acid on host cell surfaces) into the bacteria (PubMed:15743943, PubMed:22246445). NanC proteins form high-conductance channels which are open at low membrane potentials and which have a weak anion selectivity (PubMed:15743943). {ECO:0000269|PubMed:15743943, ECO:0000269|PubMed:22246445}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-15315|reaction.ecocyc.RXN-15315]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-0|reaction.ecocyc.RXN0-0]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4311|gene.b4311]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69856`
- `KEGG:ecj:JW5778;eco:b4311;`
- `GeneID:93777530;946843;`
- `GO:GO:0006811; GO:0009279; GO:0015136; GO:0015288; GO:0015478; GO:0015739; GO:0015772; GO:0046930`

## Notes

N-acetylneuraminic acid outer membrane channel protein NanC (N-acetylneuraminic acid-inducible outer membrane channel) (NanR-regulated channel) (Porin NanC)
