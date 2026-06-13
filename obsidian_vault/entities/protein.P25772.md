---
entity_id: "protein.P25772"
entity_type: "protein"
name: "ligB"
source_database: "UniProt"
source_id: "P25772"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ligB yicF b3647 JW3622"
---

# ligB

`protein.P25772`

## Static

- Type: `protein`
- Source: `UniProt:P25772`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of phosphodiester linkages between 5'-phosphoryl and 3'-hydroxyl groups in double-stranded DNA using NAD as a coenzyme and as the energy source for the reaction. {ECO:0000269|PubMed:11812821}. LigB is an NAD+-dependent DNA ligase ; LigB is implicated in base excision repair and/or mismatch repair . Purified LigB ligates a duplex DNA substrate containing a single nick; the reaction requires NAD+ and divalent cations which can be magnesium, manganese, or less effectively cobalt . A ligase-adenylate intermediate is formed when purified LigB is incubated with NAD+ ([32P-AMP]NAD+) and magnesium . LigB has sequence similarity to EG10534-MONOMER "LigA", the other NAD+-dependent DNA ligase in E. coli K-12 . LigB contains the conserved KXDG motif (motif I) which is a signature feature of the ligase/capping superfamily of covalent nucleotidyl transferases ; LigB contains a nucleotidyl transferase domain and oligomer-binding fold (OB-fold) but lacks the BRCT domain and 2 of the 4 zinc-binding cysteines that are characteristic of bacterial NAD+ ligases . LigB is significantly less active than LigA in vitro; this difference in activity is due to a differential response to the NAD+ cofactor . A K126A mutation eliminates the enzyme activity...

## Biological Role

Catalyzes (deoxyribonucleotide)n:5'-phospho-(deoxyribonucleotide)m ligase (AMP-forming, NMN-forming) (reaction.R00382), DNA-LIGASE-NAD+-RXN (reaction.ecocyc.DNA-LIGASE-NAD_-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03410` Base excision repair (KEGG)
- `eco03420` Nucleotide excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of phosphodiester linkages between 5'-phosphoryl and 3'-hydroxyl groups in double-stranded DNA using NAD as a coenzyme and as the energy source for the reaction. {ECO:0000269|PubMed:11812821}.

## Pathways

- `eco03030` DNA replication (KEGG)
- `eco03410` Base excision repair (KEGG)
- `eco03420` Nucleotide excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00382|reaction.R00382]] `KEGG` `database` - via EC:6.5.1.2
- `catalyzes` --> [[reaction.ecocyc.DNA-LIGASE-NAD_-RXN|reaction.ecocyc.DNA-LIGASE-NAD_-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3647|gene.b3647]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25772`
- `KEGG:ecj:JW3622;eco:b3647;ecoc:C3026_19760;`
- `GeneID:948164;`
- `GO:GO:0003911; GO:0006260; GO:0006281`
- `EC:6.5.1.2`

## Notes

DNA ligase B (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)] B)
