---
entity_id: "protein.P39411"
entity_type: "protein"
name: "yjjX"
source_database: "UniProt"
source_id: "P39411"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjjX b4394 JW5801"
---

# yjjX

`protein.P39411`

## Static

- Type: `protein`
- Source: `UniProt:P39411`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Phosphatase that hydrolyzes non-canonical purine nucleotides such as XTP and ITP to their respective diphosphate derivatives. Probably excludes non-canonical purines from DNA/RNA precursor pool, thus preventing their incorporation into DNA/RNA and avoiding chromosomal lesions. ITP and XTP are the best substrates, followed by GDP and dITP. Is not active on dATP and dGTP, and exhibits no phosphatase activity toward pyrimidines (CTP, TTP, UTP, dCTP, and dTTP) (PubMed:16216582). Also seems to be implicated in the resistance against the thiamine metabolism inhibitors bacimethrin and CF3-HMP (PubMed:15292217). {ECO:0000269|PubMed:16216582, ECO:0000305|PubMed:15292217}. YjjX is a phosphatase that preferentially hydrolyzes inosine triphosphate (ITP) and xanthosine triphosphate (XTP). Both ITP and XTP can be formed by oxidative deamination damage, converting an amino group of adenine or guanine to a keto group. By hydrolyzing these damaged nucleotides, YjjX may thus prevent their incorporation into RNA . A crystal structure of YjjX has been solved at 2.25 Å resolution; the protein forms a dimer in the crystal structure as well as in solution . A nucleotide binding loop was identified by combined sequence and structural alignment with other enzymes of the Maf/HAM1 superfamily and confirmed by kinetic analysis of mutant enzymes...

## Biological Role

Catalyzes ITP phosphohydrolase (reaction.R00719), xanthosine 5'-triphosphate phosphohydrolase (reaction.R12589). Component of inosine/xanthosine triphosphatase (complex.ecocyc.CPLX0-3948).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Phosphatase that hydrolyzes non-canonical purine nucleotides such as XTP and ITP to their respective diphosphate derivatives. Probably excludes non-canonical purines from DNA/RNA precursor pool, thus preventing their incorporation into DNA/RNA and avoiding chromosomal lesions. ITP and XTP are the best substrates, followed by GDP and dITP. Is not active on dATP and dGTP, and exhibits no phosphatase activity toward pyrimidines (CTP, TTP, UTP, dCTP, and dTTP) (PubMed:16216582). Also seems to be implicated in the resistance against the thiamine metabolism inhibitors bacimethrin and CF3-HMP (PubMed:15292217). {ECO:0000269|PubMed:16216582, ECO:0000305|PubMed:15292217}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00719|reaction.R00719]] `KEGG` `database` - via EC:3.6.1.73
- `catalyzes` --> [[reaction.R12589|reaction.R12589]] `KEGG` `database` - via EC:3.6.1.73
- `is_component_of` --> [[complex.ecocyc.CPLX0-3948|complex.ecocyc.CPLX0-3948]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4394|gene.b4394]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39411`
- `KEGG:ecj:JW5801;eco:b4394;ecoc:C3026_23745;`
- `GeneID:75169890;948919;`
- `GO:GO:0000166; GO:0000287; GO:0006772; GO:0009117; GO:0017111; GO:0042803; GO:0046677; GO:0103023`
- `EC:3.6.1.73`

## Notes

Inosine/xanthosine triphosphatase (ITPase/XTPase) (EC 3.6.1.73) (Non-canonical purine NTP phosphatase) (Non-standard purine NTP phosphatase) (Nucleoside-triphosphate phosphatase) (NTPase)
