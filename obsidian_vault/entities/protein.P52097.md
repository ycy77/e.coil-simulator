---
entity_id: "protein.P52097"
entity_type: "protein"
name: "tilS"
source_database: "UniProt"
source_id: "P52097"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tilS mesJ yaeN b0188 JW0183"
---

# tilS

`protein.P52097`

## Static

- Type: `protein`
- Source: `UniProt:P52097`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Ligates lysine onto the cytidine present at position 34 of the AUA codon-specific tRNA(Ile) that contains the anticodon CAU, in an ATP-dependent manner. Cytidine is converted to lysidine, thus changing the amino acid specificity of the tRNA from methionine to isoleucine. This enzyme is essential for viability. TilS is a tRNAIle-lysidine synthetase, the enzyme responsible for modifying the wobble base of the CAU anticodon of tRNAIle at the keto group in position 2 of C34 such that it exhibits proper recognition of the AUA codon rather than the AUG codon . This modification is necessary and sufficient for correct charging of the tRNA with isoleucine (not methionine) . TilS recognizes and modifies the precursor form of tRNAIle, thus ensuring the fidelity and avoiding errors in translation. Unmodified C34 is only found in pre-tRNAIle; mature tRNAIle contains the modified L34 base. Thus, it is not possible to generate mischarged Met-tRNAIleCAU . TilS recognizes the anticodon loop, the anticodon stem, and the acceptor stem of tRNA, allowing it to discriminate between tRNAIle and tRNAMet, which are structurally similar and share the same anticodon loop . t6A-modified tRNAIleCAU is a better substrate for TilS than the unmodified tRNA . Various analogs of L-lysine have been tested as inhibitors or alternative substrates for the enzyme . tilS is an essential gene...

## Biological Role

Catalyzes RXN-1961 (reaction.ecocyc.RXN-1961).

## Annotation

FUNCTION: Ligates lysine onto the cytidine present at position 34 of the AUA codon-specific tRNA(Ile) that contains the anticodon CAU, in an ATP-dependent manner. Cytidine is converted to lysidine, thus changing the amino acid specificity of the tRNA from methionine to isoleucine. This enzyme is essential for viability.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-1961|reaction.ecocyc.RXN-1961]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0188|gene.b0188]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52097`
- `KEGG:ecj:JW0183;eco:b0188;ecoc:C3026_00865;`
- `GeneID:944889;`
- `GO:GO:0002136; GO:0005524; GO:0005829; GO:0006400; GO:0032267; GO:0042802`
- `EC:6.3.4.19`

## Notes

tRNA(Ile)-lysidine synthase (EC 6.3.4.19) (tRNA(Ile)-2-lysyl-cytidine synthase) (tRNA(Ile)-lysidine synthetase)
