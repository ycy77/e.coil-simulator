---
entity_id: "protein.P0A850"
entity_type: "protein"
name: "tig"
source_database: "UniProt"
source_id: "P0A850"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:8633085}. Note=About half TF is bound to the ribosome near the polypeptide exit tunnel while the other half is free in the cytoplasm. {ECO:0000269|PubMed:8633085}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tig b0436 JW0426"
---

# tig

`protein.P0A850`

## Static

- Type: `protein`
- Source: `UniProt:P0A850`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:8633085}. Note=About half TF is bound to the ribosome near the polypeptide exit tunnel while the other half is free in the cytoplasm. {ECO:0000269|PubMed:8633085}.

## Enriched Summary

FUNCTION: Involved in protein export. Acts as a chaperone by maintaining the newly synthesized secretory and non-secretory proteins in an open conformation. Binds to 3 regions of unfolded substrate PhoA, preferring aromatic and hydrophobic residues, keeping it stretched out and unable to form aggregates (PubMed:24812405). Binds to nascent polypeptide chains via ribosomal protein L23 (PubMed:12226666). Functions as a peptidyl-prolyl cis-trans isomerase in vitro, this activity is dispensible in vivo for chaperone activity. {ECO:0000269|PubMed:12226666, ECO:0000269|PubMed:24812405, ECO:0000269|PubMed:8521806, ECO:0000269|PubMed:8633085}. Trigger factor (TF) is a ribsome-associated, ATP-independent chaperone that cooperates with downstream proteins such as EG10241-MONOMER DnaK and CPLX0-3934 GroEL-GroES in the folding of newly synthesized cytosolic proteins; TF also interacts with nascent secretory proteins and cooperates with the CPLX0-8046 SecB chaperone to usher a subset of proteins on the post-translational secretory pathway. TF is involved in protection against copper-induced protein aggregation under anaerobic growth conditions . TF exhibits peptidyl-prolyl isomerase and protein folding activity in vitro; TF associates with ribosome bound nascent cytosolic and secretory polypeptide chains in vitro...

## Biological Role

Catalyzes PEPTIDYLPROLYL-ISOMERASE-RXN (reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN).

## Annotation

FUNCTION: Involved in protein export. Acts as a chaperone by maintaining the newly synthesized secretory and non-secretory proteins in an open conformation. Binds to 3 regions of unfolded substrate PhoA, preferring aromatic and hydrophobic residues, keeping it stretched out and unable to form aggregates (PubMed:24812405). Binds to nascent polypeptide chains via ribosomal protein L23 (PubMed:12226666). Functions as a peptidyl-prolyl cis-trans isomerase in vitro, this activity is dispensible in vivo for chaperone activity. {ECO:0000269|PubMed:12226666, ECO:0000269|PubMed:24812405, ECO:0000269|PubMed:8521806, ECO:0000269|PubMed:8633085}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN|reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0436|gene.b0436]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A850`
- `KEGG:ecj:JW0426;eco:b0436;ecoc:C3026_02135;`
- `GeneID:75170454;75202861;945081;`
- `GO:GO:0003755; GO:0005829; GO:0006457; GO:0009408; GO:0015031; GO:0016020; GO:0042802; GO:0043022; GO:0043335; GO:0044183; GO:0051083; GO:0051301; GO:1990169`
- `EC:5.2.1.8`

## Notes

Trigger factor (TF) (EC 5.2.1.8) (PPIase)
