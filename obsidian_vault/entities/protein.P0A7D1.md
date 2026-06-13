---
entity_id: "protein.P0A7D1"
entity_type: "protein"
name: "pth"
source_database: "UniProt"
source_id: "P0A7D1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00083, ECO:0000305|PubMed:4898482, ECO:0000305|PubMed:9303320}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pth rap b1204 JW1195"
---

# pth

`protein.P0A7D1`

## Static

- Type: `protein`
- Source: `UniProt:P0A7D1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00083, ECO:0000305|PubMed:4898482, ECO:0000305|PubMed:9303320}.

## Enriched Summary

FUNCTION: Hydrolyzes ribosome-free peptidyl-tRNAs (with 1 or more amino acids incorporated), which drop off the ribosome during protein synthesis, or as a result of ribosome stalling (PubMed:4866985, PubMed:4898482, PubMed:9303320). {ECO:0000255|HAMAP-Rule:MF_00083, ECO:0000269|PubMed:4866985, ECO:0000269|PubMed:4898482, ECO:0000269|PubMed:9303320}.; FUNCTION: The hydrolysis rate of peptidyl-tRNAs depends on the peptide chain length, with peptidyl-tRNAs with up to 5 residues being a better substrate; Gly(4)-Phe-tRNA(Phe) is hydrolyzed faster than Gly(2)-Phe-tRNA(Phe) which is hydrolyzed faster than Gly-Phe-tRNA(Phe) (PubMed:4898482). Also acts on singly charged tRNAs including charged tRNA(Ile), tRNA(Leu), tRNA(Ser), tRNA(Thr) and tRNA(Val) (PubMed:4866985). Acts on charged tRNA(Lys) (PubMed:9303320). Unblocked charged tRNAs are very poor substrates, discrimination is mediated by Asn-11 which binds to the main-chain carbonyl of the penultimate residue (PubMed:21718701). Acts on charged tRNA(Ala) (PubMed:22923517). Involved in lambda inhibition of host protein synthesis (PubMed:1833189). Pth activity may, directly or indirectly, be the target for lambda bar RNA leading to rap cell death (PubMed:1833189). {ECO:0000269|PubMed:1833189, ECO:0000269|PubMed:21718701, ECO:0000269|PubMed:22923517, ECO:0000269|PubMed:4866985, ECO:0000269|PubMed:4898482, ECO:0000269|PubMed:9303320}...

## Biological Role

Catalyzes AMINOCYL-TRNA-HYDROLASE-RXN (reaction.ecocyc.AMINOCYL-TRNA-HYDROLASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Hydrolyzes ribosome-free peptidyl-tRNAs (with 1 or more amino acids incorporated), which drop off the ribosome during protein synthesis, or as a result of ribosome stalling (PubMed:4866985, PubMed:4898482, PubMed:9303320). {ECO:0000255|HAMAP-Rule:MF_00083, ECO:0000269|PubMed:4866985, ECO:0000269|PubMed:4898482, ECO:0000269|PubMed:9303320}.; FUNCTION: The hydrolysis rate of peptidyl-tRNAs depends on the peptide chain length, with peptidyl-tRNAs with up to 5 residues being a better substrate; Gly(4)-Phe-tRNA(Phe) is hydrolyzed faster than Gly(2)-Phe-tRNA(Phe) which is hydrolyzed faster than Gly-Phe-tRNA(Phe) (PubMed:4898482). Also acts on singly charged tRNAs including charged tRNA(Ile), tRNA(Leu), tRNA(Ser), tRNA(Thr) and tRNA(Val) (PubMed:4866985). Acts on charged tRNA(Lys) (PubMed:9303320). Unblocked charged tRNAs are very poor substrates, discrimination is mediated by Asn-11 which binds to the main-chain carbonyl of the penultimate residue (PubMed:21718701). Acts on charged tRNA(Ala) (PubMed:22923517). Involved in lambda inhibition of host protein synthesis (PubMed:1833189). Pth activity may, directly or indirectly, be the target for lambda bar RNA leading to rap cell death (PubMed:1833189). {ECO:0000269|PubMed:1833189, ECO:0000269|PubMed:21718701, ECO:0000269|PubMed:22923517, ECO:0000269|PubMed:4866985, ECO:0000269|PubMed:4898482, ECO:0000269|PubMed:9303320}.; FUNCTION: Catalyzes the release of premature peptidyl moieties from peptidyl-tRNA molecules trapped in stalled 50S ribosomal subunits, and thus maintains levels of free tRNAs and 50S ribosomes (PubMed:38183984). Releases Ala-tailed nascent peptides from stalled 50S ribosomal subunits; in the absence of Ala tails less peptide release occurs (PubMed:38183984). Addition of 3 Ala residues suffices to stimulate peptide release from stalled 50S ribosomal subunits, although better release occurs with 7 residues (PubMed:38183984). Poly-Ala and poly-Ser are the most efficient residue in promoting peptide release, other amino acid heptad tails are less efficient (PubMed:38183984). {ECO:0000269|PubMed:38183984}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.AMINOCYL-TRNA-HYDROLASE-RXN|reaction.ecocyc.AMINOCYL-TRNA-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1204|gene.b1204]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7D1`
- `KEGG:ecj:JW1195;eco:b1204;ecoc:C3026_07080;`
- `GeneID:93775269;945765;`
- `GO:GO:0000049; GO:0004045; GO:0005737; GO:0006515; GO:0071236; GO:0072344`
- `EC:3.1.1.29`

## Notes

Peptidyl-tRNA hydrolase (Pth) (EC 3.1.1.29) [Cleaved into: Peptidyl-tRNA hydrolase, N-terminally processed]
