---
entity_id: "protein.P36979"
entity_type: "protein"
name: "rlmN"
source_database: "UniProt"
source_id: "P36979"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmN yfgB b2517 JW2501"
---

# rlmN

`protein.P36979`

## Static

- Type: `protein`
- Source: `UniProt:P36979`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates position 2 of adenine 2503 in 23S rRNA and position 2 of adenine 37 in tRNAs. m2A2503 modification seems to play a crucial role in the proofreading step occurring at the peptidyl transferase center and thus would serve to optimize ribosomal fidelity. Unmodified tRNA is not a suitable substrate for RlmN, which suggests that RlmN works in a late step during tRNA maturation. {ECO:0000269|PubMed:18025251, ECO:0000269|PubMed:21415317, ECO:0000269|PubMed:22891362}. RlmN is the methyltransferase responsible for methylation of 23S rRNA at the C2 position of the A2503 nucleotide . The enzyme can utilize free 23S rRNA as the substrate, but not the fully assembled large ribosomal subunit . RlmN is also responsible for methylation of certain tRNAs at the C2 position of A37 . RlmN substrates and modification sites within the substrates have been determined . RlmN belongs to the Cfr/RlmN family of the "radical SAM" superfamily of proteins . The reaction requires two molecules of SAM, one as the methyl group donor, and the second as the source of the 5'-deoxyadenosyl radical . The cysteine residues of the 4Fe-4S cluster-binding motif are essential for activity of RlmN and coordinate one 4Fe-4S cluster...

## Biological Role

Catalyzes RXN-11586 (reaction.ecocyc.RXN-11586), RXN0-7007 (reaction.ecocyc.RXN0-7007). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

FUNCTION: Specifically methylates position 2 of adenine 2503 in 23S rRNA and position 2 of adenine 37 in tRNAs. m2A2503 modification seems to play a crucial role in the proofreading step occurring at the peptidyl transferase center and thus would serve to optimize ribosomal fidelity. Unmodified tRNA is not a suitable substrate for RlmN, which suggests that RlmN works in a late step during tRNA maturation. {ECO:0000269|PubMed:18025251, ECO:0000269|PubMed:21415317, ECO:0000269|PubMed:22891362}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-11586|reaction.ecocyc.RXN-11586]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7007|reaction.ecocyc.RXN0-7007]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2517|gene.b2517]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36979`
- `KEGG:ecj:JW2501;eco:b2517;ecoc:C3026_13955;`
- `GeneID:93774619;946249;`
- `GO:GO:0000049; GO:0002935; GO:0005829; GO:0019843; GO:0030488; GO:0046677; GO:0046872; GO:0051539; GO:0070040; GO:0070475`
- `EC:2.1.1.192`

## Notes

Dual-specificity RNA methyltransferase RlmN (EC 2.1.1.192) (23S rRNA (adenine(2503)-C(2))-methyltransferase) (23S rRNA m2A2503 methyltransferase) (Ribosomal RNA large subunit methyltransferase N) (tRNA (adenine(37)-C(2))-methyltransferase) (tRNA m2A37 methyltransferase)
