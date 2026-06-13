---
entity_id: "protein.Q46896"
entity_type: "protein"
name: "ygbT"
source_database: "UniProt"
source_id: "Q46896"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:21219465}. Note=In 15% of cell localizes to discrete nucleoid foci (probable DNA damage sites) upon treatment with mitomycin C (MMC) for 2 hours (PubMed:21219465). {ECO:0000269|PubMed:21219465}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygbT cas1 b2755 JW2725"
---

# ygbT

`protein.Q46896`

## Static

- Type: `protein`
- Source: `UniProt:Q46896`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:21219465}. Note=In 15% of cell localizes to discrete nucleoid foci (probable DNA damage sites) upon treatment with mitomycin C (MMC) for 2 hours (PubMed:21219465). {ECO:0000269|PubMed:21219465}.

## Enriched Summary

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids) (PubMed:21255106, PubMed:24793649, PubMed:24920831). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA). The Cas1-Cas2 complex is involved in CRISPR adaptation, the first stage of CRISPR immunity, being required for the addition/removal of CRISPR spacers at the leader end of the CRISPR locus (PubMed:24793649, PubMed:24920831, PubMed:25707795). The Cas1-Cas2 complex introduces staggered nicks into both strands of the CRISPR array near the leader repeat and joins the 5'-ends of the repeat strands with the 3'-ends of the new spacer sequence (PubMed:24920831). Spacer DNA integration requires supercoiled target DNA and 3'-OH ends on the inserted (spacer) DNA and probably initiates with a nucleophilic attack of the C 3'-OH end of the protospacer on the minus strand of the first repeat sequence (PubMed:25707795). Expression of Cas1-Cas2 in a strain lacking both genes permits spacer acquisition (PubMed:24793649, PubMed:24920831). Non-specifically binds DNA; the Cas1-Cas2 complex preferentially binds CRISPR-locus DNA (PubMed:24793649)...

## Biological Role

Component of multifunctional nuclease Cas1 (complex.ecocyc.CPLX0-7914), Cas1-Cas2 complex (complex.ecocyc.CPLX0-8174).

## Annotation

FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids) (PubMed:21255106, PubMed:24793649, PubMed:24920831). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA). The Cas1-Cas2 complex is involved in CRISPR adaptation, the first stage of CRISPR immunity, being required for the addition/removal of CRISPR spacers at the leader end of the CRISPR locus (PubMed:24793649, PubMed:24920831, PubMed:25707795). The Cas1-Cas2 complex introduces staggered nicks into both strands of the CRISPR array near the leader repeat and joins the 5'-ends of the repeat strands with the 3'-ends of the new spacer sequence (PubMed:24920831). Spacer DNA integration requires supercoiled target DNA and 3'-OH ends on the inserted (spacer) DNA and probably initiates with a nucleophilic attack of the C 3'-OH end of the protospacer on the minus strand of the first repeat sequence (PubMed:25707795). Expression of Cas1-Cas2 in a strain lacking both genes permits spacer acquisition (PubMed:24793649, PubMed:24920831). Non-specifically binds DNA; the Cas1-Cas2 complex preferentially binds CRISPR-locus DNA (PubMed:24793649). Highest binding is seen to a dual forked DNA complex with 3'-overhangs and a protospacer-adjacent motif-complement specifically positioned (PubMed:26478180). The protospacer DNA lies across a flat surface extending from 1 Cas1 dimer, across the Cas2 dimer and contacting the other Cas1 dimer; the 23 bp-long ds section of the DNA is bracketed by 1 Tyr-22 from each of the Cas1 dimers (PubMed:26478180, PubMed:26503043). Cas1 cuts within the 3'-overhang, to generate a 33-nucleotide DNA that is probably incorporated into the CRISPR leader by a cut-and-paste mechanism (PubMed:26478180). Cas1 alone endonucleolytically cleaves linear ssRNA, ssDNA and short (34 base) dsDNA as well as branched DNA substrates such as Holliday junctions, replication forks and 5'-flap DNA substrates (PubMed:21219465). In vitro catalyzes a concerted transesterification reaction on branched DNA, as would be expected during integration of protospacers into the CRISPR leader sequence; Cas2 is not required in vitro. This reaction requires a 3'-OH group at the branch point (PubMed:26284603). Genetic interactions suggest Cas1 interacts with components of the RecBC and RuvB DNA repair systems (PubMed:21219465). {ECO:0000269|PubMed:21219465, ECO:0000269|PubMed:21255106, ECO:0000269|PubMed:24793649, ECO:0000269|PubMed:24920831, ECO:0000269|PubMed:25707795, ECO:0000269|PubMed:26284603, ECO:0000269|PubMed:26478180}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7914|complex.ecocyc.CPLX0-7914]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8174|complex.ecocyc.CPLX0-8174]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2755|gene.b2755]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46896`
- `KEGG:ecj:JW2725;eco:b2755;ecoc:C3026_15145;`
- `GeneID:947228;`
- `GO:GO:0003677; GO:0004519; GO:0005737; GO:0006281; GO:0006974; GO:0008821; GO:0017108; GO:0042802; GO:0042803; GO:0043571; GO:0046872; GO:0051607; GO:0099048`
- `EC:3.1.-.-`

## Notes

CRISPR-associated endonuclease Cas1 (EC 3.1.-.-)
